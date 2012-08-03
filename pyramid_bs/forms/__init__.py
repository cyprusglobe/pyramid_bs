from wtforms import Form


class AjaxForm(Form):
    def json_errors(self, obj=None):
        field_errors = {}
        validated = self.validate(json_validation_obj=obj)
        for name in self.data:
            field = self.__getattribute__(name)
            if field.errors:
                field_errors[name] = {
                    'error': True,
                    'message': field.errors[0],
                    'color': field.color if 'color' in vars(field) else None
                }
            else:
                message = field.message if 'message' in vars(field) else None
                if message:
                    field_errors[name] = {
                        'error': False,
                        'message': message,
                        'color': field.color if 'color' in vars(field) else None
                    }
        return {
            'fields': field_errors,
            'validated': validated
        }

    def validate(self, json_validation_obj=None, **kwargs):
        # strip any whitespace from strings before validation
        for field in self:
            if isinstance(field.data, basestring):
                field.data = field.data.strip()

            for name, func in self.json_validators:
                if name == field.name:
                    result = func(field.data, json_validation_obj)
                    if result:
                        error = result[0]
                        message = result[1]
                        color = result[2] if len(result) > 2 else ''

                        if error is True:
                            # add the error message
                            field.process_errors.append(message)
                            field.color = color
                        else:
                            # add the happy message
                            if message:
                                field.message = message
                                field.color = color

        return super(AjaxForm, self).validate(**kwargs)
