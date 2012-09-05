<%inherit file="layout.mako"/>
<%namespace name="form_utils" file="/form_utils.mako"/>
<form id="request_form" action="" method="POST" class="form-horizontal" autocomplete="off">
    <input type="hidden" name="_csrf" value="${request.csrf_token}">
    <div class="row">
        <div class="span12">
        <h2>Request Permission For Special Access</h2>
        <br/>
            <div class="well">
                <p>This page will allow you to request permission for higher permission</p>
                <em>Your request will be sent for approval by the admins</em>
                <br/>
                <br/>
                <h4>Please select the group you would like access too</h4>
                <br/>
                ${form_utils.field(form, 'request', class_="span2")}
                <br/>
                <em>Please submit your request below and an admin will look over it</em>
                <br/>
                <br/>
                <div class="row">
                    <button type="submit" class="btn btn-success"><i class="icon-ok"></i> Submit</button>
                    <a href="javascript:;" class="btn"
                        onclick="window.location = '${request.route_url('user_list')}';"><i class="icon-ban-circle"></i> Cancel</a>
                </div>
            </div>
        </div>
    </div>
</form>
