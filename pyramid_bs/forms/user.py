from ..forms import AjaxForm

from ..forms.fields import (
    loginField,
    passwordField,
    editPasswordField,
    confirmField,
    firstNameField,
    lastNameField,
    phoneField,
    emailField,
    securedField,
    basicField,
)

from ..models.user import User


# login exists validator
def login_exists(field_data, edit_user):
    user = User.by_login(field_data)

    # the user exists
    if user:
        # not an update
        if user != edit_user:
            return (True, 'Sorry this login already exists!')
        #else:
        #    return (False, 'Keepting the same login')
    else:
        if not edit_user:
            return (False, 'This user is available.')
        else:
            return (False, 'Note: You are changing the login', 'blue')


class AddForm(AjaxForm):
    json_validators = [('login', login_exists)]
    login = loginField
    password = passwordField
    confirm = confirmField
    first_name = firstNameField
    last_name = lastNameField
    phone = phoneField
    email = emailField
    secured = securedField
    basic = basicField


class EditForm(AjaxForm):
    json_validators = [('login', login_exists)]
    login = loginField
    password = editPasswordField
    confirm = confirmField
    first_name = firstNameField
    last_name = lastNameField
    phone = phoneField
    email = emailField
    secured = securedField
    basic = basicField
