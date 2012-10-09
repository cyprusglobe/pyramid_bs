<%inherit file="layout.mako"/>
<%namespace name="form_utils" file="/form_utils.mako"/>

<div class="row">
    <div class="span12">
        ${len(users)} results
        <table class="table table-striped table-bordered">
            <thead>
                <tr>
                    <th>Login</th>
                    <th>First_Name</th>
                    <th>Last Name</th>
                    <th>Phone</th>
                    <th>Email</th>
                    <th>Groups</th>
                </tr>
            </thead>
            %for user in users:
                <tbody>
                    <tr>
                        <td>
                            ${user.login}
                            <a class="" href="${request.route_url('user_edit', user_id=user.id)}"><i class="icon-edit"></i></a>
                            <a class="" data-target="#confirm-modal" data-toggle="modal" href="javascript:;"
                                onclick="$('#confirm-modal #delete').attr('href', '/user/' + ${user.id} + '/delete');"><i class="icon-trash"></i></a>
                        </td>
                        <td>${user.first_name}</td>
                        <td>${user.last_name}</td>
                        <td>${user.phone}</td>
                        <td>${user.email}</td>
                        <td>
                        %for group in user.mygroups:
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
<!--
${form_utils.ajax_form('group_form')}
-->
