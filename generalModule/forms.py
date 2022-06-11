from django.contrib.auth.forms import AuthenticationForm


class CustomLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Ingrese el nombre de usuario'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Ingrese su contraseña'}
        )
