<%inherit file="/layout.mako"/>
${self.confrim_delete("Are you sure you want to delete this user?")}

<div class="row">
    <div class="span12">
        %if request.route_url('user_list') in request.url:
            <h2>Users</h2>
            <a href="${request.route_url('user_edit', user_id=0)}" class="btn btn-mini pull-right" style="margin-left:10px;"><i class="icon-user"></i> Create</a>
        %elif request.route_url('user_list')[:-1] in request.url:
            %if user:
                <h2>Edit User</h2>
                <a href="${request.route_url('user_edit', user_id=0)}" class="btn btn-mini pull-right" style="margin-left:10px;"><i class="icon-user"></i> Create</a>
                <a class="btn btn-mini btn-danger pull-right" data-target="#confirm-modal" data-toggle="modal" href="javascript:;"
                    onclick="$('.qtip').qtip('hide').qtip('disable'); $('#confirm-modal #delete').attr('href', '/user/' + ${user.id} + '/delete');"><i class="icon-trash"></i> Delete</a>
            %else:
                <h2>New User</h2>
            %endif
        %endif
    </div>
</div>

${next.body()}
