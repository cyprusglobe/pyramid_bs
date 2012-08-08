from wtforms import (
    BooleanField,
    PasswordField,
    SelectField,
    TextField,
    validators,
)

loginField = TextField('Login', [validators.Length(min=4, max=10)])

passwordField = PasswordField('Password', [validators.Length(min=6, max=15)])

editPasswordField = PasswordField('Password', [validators.Optional(),
                                              validators.Length(min=6, max=15)])

confirmField = PasswordField('Confrim', [validators.EqualTo(
    'password', message='Passwords must match')])

firstNameField = TextField('First Name', [validators.Length(min=2, max=25)])

lastNameField = TextField('Last_name', [validators.Length(min=2, max=25)])

phoneField = TextField('Phone', [])

emailField = TextField('Email', [validators.email()])

securedField = BooleanField(u'Secured', [])

basicField = BooleanField(u'Basic', [])

requestField = SelectField('Permission', choices=[(u'viewer', u'Viewer'), (u'editor', u'Editor'), (u'admin', u'Admin')])
