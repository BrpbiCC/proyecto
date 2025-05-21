from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Usuario, TipoUsuario

class RegistroClienteForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'correo']

    def clean_correo(self):
        correo = self.cleaned_data['correo']
        if Usuario.objects.filter(correo=correo).exists():
            raise ValidationError("Ya existe un usuario con este correo electrónico.")
        return correo

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password is not None and password != confirm_password:
            raise ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        try:
            tipo_cliente = TipoUsuario.objects.get(tipo_nombre='cliente')
            user.tipo_usuario = tipo_cliente
        except TipoUsuario.DoesNotExist:
            # Handle the case where 'cliente' TipoUsuario doesn't exist.
            # You might want to create it here or handle the error appropriately.
            print("Error: El tipo de usuario 'cliente' no existe. Asegúrate de crearlo.")
            raise
        if commit:
            user.save()
        return user