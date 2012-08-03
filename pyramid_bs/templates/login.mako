<%inherit file="/layout.mako"/>
<%namespace name="form_utils" file="form_utils.mako"/>

<form id="login_form" action="" method="POST" class="form-horizontal">
   <input type="hidden" name="_csrf" value="${request.csrf_token}">
    <div class="row">
        <div class="offset1">
            <h4>Sign in</h4>
            ${form_utils.field(form, 'login', class_="span2")}
            ${form_utils.field(form, 'password', class_="span2")}
        </div>
    </div>
    <div class="row">
        <div class="offset4">
            <button type="submit" class="btn btn-success"><i class="icon-ok"></i> Submit</button>
            <a href="javascript:;" class="btn"
                onclick="window.location = '${request.route_url('index')}';"><i class="icon-ban-circle"></i> Cancel</a>
        </div>
    </div>
</form>

${form_utils.ajax_form('login_form')}
