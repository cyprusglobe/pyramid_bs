<%inherit file="layout.mako"/>

<div class="row">
    <div class="span12">
        ${len(users)} results
        <table class="table table-striped table-bordered table-condensed">
            <thead>
                <th>Login</th>
                <th>First_Name</th>
                <th>Last Name</th>
                <th>Phone</th>
                <th>Email</th>
            </thead>
            %for user in users:
                <tbody>
                    <tr>
                        <td>
                            <a href="${request.route_url('user_edit', user_id=user.id)}">${user.login}</a>
                            <a class="pull-right" data-target="#confirm-modal" data-toggle="modal" href="javascript:;"
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
