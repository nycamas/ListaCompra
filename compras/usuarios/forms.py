from django import forms
from django.contrib.auth.models import User
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['username', 'password', 'status']

    def save(self, commit=True):
        # Crear el usuario de Django
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = User.objects.create_user(username=username, password=password)

        # Crear el objeto Usuario y enlazarlo al nuevo User
        usuario = super().save(commit=False)
        usuario.usuario = user
        if commit:
            usuario.save()
        return usuario

# Editar usuario: solo se modifica el status
class UsuarioEditForm(forms.ModelForm):
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    class Meta:
        model = Usuario
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.usuario:
            self.fields['username'].initial = self.instance.usuario.username
            self.fields['username'].widget.attrs['readonly'] = True
            self.fields['username'].widget.attrs['class'] = 'form-control-plaintext'