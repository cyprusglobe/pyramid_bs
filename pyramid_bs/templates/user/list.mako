<%inherit file="layout.mako"/>
<%namespace name="form_utils" file="/form_utils.mako"/>

<div class="row">
    <div class="span12">
        ${len(users)} results
        <div class="clearfix"></div>
        <br/>
            %for user in users:
                <div class="span4">
                    <div class="well">
                        <img src="${user.gravatar(user.email)}" alt="Gravatar" class="pull-left" style="padding-right: 10px;"/>
                        <a href="${request.route_url('user_view', user_id=user.id)}">${user.first_name}, ${user.last_name}</a>
                        <div class="pull-right">
                            <a class="" href="${request.route_url('user_edit', user_id=user.id)}"><i class="icon-edit"></i></a>
                            <a class="" data-target="#confirm-modal" data-toggle="modal" href="javascript:;"
                                onclick="$('#confirm-modal #delete').attr('href', '/user/' + ${user.id} + '/delete');"><i class="icon-trash"></i></a>
                        </div>
                        <br/>
                        %for group in user.mygroups:
                            %if group.name == 'secured':
                                <span class="label label-important">${group.name}</span>
                            %else:
                                <span class="label label-info">${group.name}</span>
                            %endif
                        %endfor
                    </div>
                </div>
            %endfor
    </div>
</div>
<!--
${form_utils.ajax_form('group_form')}
-->
