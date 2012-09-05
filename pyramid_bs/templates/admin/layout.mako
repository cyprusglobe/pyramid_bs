<%inherit file="/layout.mako"/>
${self.confrim_delete("Are you sure you want to delete this user?")}

<div class="row">
    <div class="span12">
        %if request.route_url('admin_list') in request.url:
            <h2>Admins</h2>
            <a href="${request.route_url('user_edit', user_id=0)}" class="btn btn-mini pull-right" style="margin-left:10px;"><i class="icon-user"></i> Create</a>
        %elif request.route_url('admin_list')[:-1] in request.url:
            %if user:
                <h2>Edit Admin</h2>

                <a class="btn btn-mini btn-danger pull-right" data-target="#confirm-modal" data-toggle="modal" href="javascript:;"
                    onclick="$('.qtip').qtip('hide').qtip('disable'); $('#confirm-modal #delete').attr('href', '/user/' + ${user.id} + '/delete');"><i class="icon-trash"></i> Delete</a>
            %else:
                <h2>New Admin</h2>
            %endif
        %endif
    </div>
</div>

${next.body()}
