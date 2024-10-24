from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: pedro"
            }
        )
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Senha"
            }
        ) 
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome completo",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: Pedro Silva"
            }
        )
    )
    username = forms.CharField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(  # Use EmailInput para email
            attrs={
                "class": "form-control",
                "placeholder": "Ex: pedro@gmail.com"
            }
        )
    )
    senha_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Senha"
            }
        )
    )
    senha_2 = forms.CharField(
        label="Confirmar Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Senha Novamente"
            }
        )
    )