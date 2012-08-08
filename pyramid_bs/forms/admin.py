from ..forms import AjaxForm

from ..forms.fields import (
    requestField,
)


class RequestForm(AjaxForm):
    json_validators = []
    request = requestField
