from ..forms import AjaxForm

from ..forms.fields import (
    loginField,
    passwordField,
)


class LoginForm(AjaxForm):
    json_validators = []
    login = loginField
    password = passwordField
