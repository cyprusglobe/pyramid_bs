<%inherit file="layout.mako"/>
<%namespace name="form_utils" file="/form_utils.mako"/>
<div class="row">
    <div class="span12">
            <div class="well">
                %if gravatar:
                <div class="row">
                    <div class="span1">
                        <img src="${gravatar}" alt="Gravatar" class="pull-left" style="margin:8px;"/>
                    </div>
                    <div class="span3">
                        <p class="muted">${user.first_name}, ${user.last_name} <a class="" href="${request.route_url('user_edit', user_id=user.id)}"><i class="icon-edit"></i></a></p>
                        <p class="muted">${user.phone}</p>
                        <p class="muted">${user.email}</p>
                        %for group in user.mygroups:
                            %if group.name == 'secured':
                                <span class="label label-important">${group.name}</span>
                            %else:
                                <span class="label label-info">${group.name}</span>
                            %endif
                        %endfor
                    </div>
                </div>
                %endif
            </div>
    </div>
</div>
