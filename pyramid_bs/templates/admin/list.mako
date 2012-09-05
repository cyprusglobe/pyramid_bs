<%inherit file="layout.mako"/>
<%namespace name="form_utils" file="/form_utils.mako"/>

<div class="row pull-right">
    <div class="span2"
        <form id="request_form" action="" method="POST" class="form-horizontal" autocomplete="off">
            <input type="hidden" name="_csrf" value="${request.csrf_token}">
            ${form_utils.field(form, 'group', class_="span2")}
        </form>
    </div>
</div>
<div class="row">
    <div class="span12">
        ${len(admins)} results
        <table class="table table-striped table-bordered table-condensed">
            <thead>
                <th>Login</th>
                <th>First_Name</th>
                <th>Last Name</th>
                <th>Phone</th>
                <th>Email</th>
            </thead>
            %for admin in admins:
                <tbody>
                    <tr>
                        <td>
                            <a href="#">${admin.login}</a>
                        </td>
                        <td>${admin.first_name}</td>
                        <td>${admin.last_name}</td>
                        <td>${admin.phone}</td>
                        <td>${admin.email}</td>
                        <td>
                        %for group in admin.mygroups:
                            %if group.name == 'secured':
                                <span class="label label-important">${group.name}</span>
                            %else:
                                <span class="label label-info">${group.name}</span>
                            %endif
                        %endfor
                        </td>
                    </tr>
                </tbody>
            %endfor
        </table>
    </div>
</div>
