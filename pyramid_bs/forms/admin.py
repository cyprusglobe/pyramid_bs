from ..forms import AjaxForm

from ..forms.fields import (
    groupField,
)


class RequestForm(AjaxForm):
    json_validators = []
    group = groupField
