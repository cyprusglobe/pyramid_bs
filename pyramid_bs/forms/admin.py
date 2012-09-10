from ..forms import AjaxForm

from ..forms.fields import (
    groupField,
)


class AdminForm(AjaxForm):
    json_validators = []
    group = groupField
