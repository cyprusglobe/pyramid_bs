<%inherit file="layout.mako"/>
<%namespace name="form_utils" file="/form_utils.mako"/>
<!--
<form id="user_form" action="" method="POST" class="form-horizontal" autocomplete="off">
   <input type="hidden" name="_csrf" value="${request.csrf_token}">
    <div class="row">
        <div class="offset1">
            <h4>Login</h4>
            ${form_utils.field(form, 'login', class_="span4")}
            ${form_utils.field(form, 'password', class_="span4")}
            ${form_utils.field(form, 'confirm', class_="span4")}

            <h4>Contact</h4>
            ${form_utils.field(form, 'first_name', class_="span4")}
            ${form_utils.field(form, 'last_name', class_="span4")}
            ${form_utils.field(form, 'phone', class_="span4")}
            ${form_utils.field(form, 'email', class_="span4")}

            ${form_utils.check_field(form, 'secured')}
            ${form_utils.check_field(form, 'basic')}
        </div>
    </div>
    <div class="row">
        <div class="offset4">
            <button type="submit" class="btn btn-success"><i class="icon-ok"></i> Submit</button>
            <a href="javascript:;" class="btn"
                onclick="window.location = '${request.route_url('user_list')}';"><i class="icon-ban-circle"></i> Cancel</a>
        </div>
    </div>
-->
<ul class="nav nav-tabs" id="myTab">
  <li class="active"><a href="#home">Login Information</a></li>
  <li><a href="#profile">Contact Information</a></li>
</ul>

<form id="user_form" action="" method="POST" class="form-horizontal" autocomplete="off">
    <input type="hidden" name="_csrf" value="${request.csrf_token}">
    <div class="tab-content">
        <div class="tab-pane active" id="home">
                ${form_utils.field(form, 'login', class_="span4")}
                ${form_utils.field(form, 'password', class_="span4")}
                ${form_utils.field(form, 'confirm', class_="span4")}
        </div>
        <div class="tab-pane" id="profile">
                ${form_utils.field(form, 'first_name', class_="span4")}
                ${form_utils.field(form, 'last_name', class_="span4")}
                ${form_utils.field(form, 'phone', class_="span4")}
                ${form_utils.field(form, 'email', class_="span4")}

                ${form_utils.check_field(form, 'secured')}
                ${form_utils.check_field(form, 'basic')}
        </div>
    </div>
    <div class="row">
        <div class="offset2">
            <button type="submit" class="btn btn-success"><i class="icon-ok"></i> Submit</button>
            <a href="javascript:;" class="btn"
                onclick="window.location = '${request.route_url('user_list')}';"><i class="icon-ban-circle"></i> Cancel</a>
        </div>
    </div>
</form>
${form_utils.ajax_form('user_form', ajax_fields=['login'])}

<script type="text/javascript">
    $('#myTab a').click(function (e) {
      e.preventDefault();
      $(this).tab('show');
    })
</script>
