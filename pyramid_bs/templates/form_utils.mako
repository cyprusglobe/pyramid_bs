<%def name="ajax_form(form_id, ajax_fields=[])">
    <script type="text/javascript" charset="utf-8">
        function validationTip(field, data) {
            if (!data || !data.message) {
                return;
            }

            if (data.color) {
                var classes = 'ui-tooltip-' + data.color + ' small'
            } else {
                var classes = data.error === false ? 'ui-tooltip-green small' : 'ui-tooltip-red small'
            }

            field.qtip({
                content: data.message,
                position: {
                    my: 'center left',
                    at: 'center right'
                },
                style: {
                    classes: classes,
                    def:false,
                    width: 220
                },
                show: true,
                hide: 'blur'
            });
            field.qtip('show');
        }

        function validateForm() {
            var form = $(this)
            $.ajax(
            {
                type: "GET",
                url: form.attr("action"),
                cache: false,
                dataType: "json",
                data: form.serialize(),
                form: form,
                success: function(data) {
                    if (data.validated === true) {
                        form.unbind("submit", validateForm);
                        form.submit();
                    } else {
                        for (var name in data.fields) {
                            validationTip($('#' + name), data.fields[name]);
                        }
                    }
                },
                error: function(xhr, status, error) {
                    this.set('content.text', '(' + status + ', ' + error + ')');
                },
                beforeSend: function() {
                    $('.qtip').qtip('hide').qtip('disable');
                    return true;
                }
            });
            return false;
        }

        function validateField() {
            var field = $(this);
            var form = $(this).closest('form');
            var name = field.attr('name')
            if (!field.val()) {
                return false;
            }
            $.ajax(
            {
                type: "GET",
                url: form.attr("action") + '?validate=' + name,
                cache: false,
                dataType: "json",
                data: form.serialize(),
                form: form,
                success: function(data) {
                    validationTip(field, data.fields[name]);
                },
                beforeSend: function() {
                    //$('.qtip').qtip('hide');
                    return true;
                }
            });
            return false;
        }

        $(document).ready(function()
        {
            var form = $("#${form_id}");
            form.bind("submit", validateForm);

            %for field in ajax_fields:
                $("#${field}").bind("blur", validateField);
            %endfor
        });
    </script>
</%def>

<%def name="field(form, field, bottom=7, **kwargs)">
    %if form.__getattribute__(field).errors:
        <div class="control-group error" style="margin-bottom:${bottom}px;">
    %else:
        <div class="control-group" style="margin-bottom:${bottom}px;">
    %endif

        %if 'label' in kwargs:
            <label class="control-label" style="margin-bottom:${bottom}px;" for="${field}">${kwargs.pop('label')}:</label>
        %else:
            <label class="control-label" style="margin-bottom:${bottom}px;" for="${field}">${form.__getattribute__(field).label}</label>
        %endif
        <div class="controls">
            ${form.__getattribute__(field)(**kwargs)}
            %if form.__getattribute__(field).errors:
                <span class="help-inline">${'<br/>'.join(form.__getattribute__(field).errors)}</span>
            %endif
        </div>
    </div>
</%def>

<%def name="check_field(form, field, bottom=5, **kwargs)">
    %if form.__getattribute__(field).errors:
        <div class="control-group error" style="margin-bottom:${bottom}px;">
    %else:
        <div class="control-group" style="margin-bottom:${bottom}px;">
    %endif

        <label class="control-label" style="margin-bottom:${bottom}px;" for="${field}">${form.__getattribute__(field).label}</label>
        <div class="controls">
            <label class="fieldbox" style="margin-bottom:${bottom}px;">
                ${form.__getattribute__(field)(**kwargs)}
            </label>
            <span class="help-inline">${'<br/>'.join(form.__getattribute__(field).errors)}</span>
        </div>
    </div>
</%def>
