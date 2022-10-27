from app.view.example import ExampleViewHandler
from app.view import auth

handlers = [
    (r'/example', ExampleViewHandler),
    (r'/users', auth.UserViewHandler),
    (r'/permissions', auth.PermissionViewHandler),
    (r'/permission_groups', auth.PermissionGroupViewHandler),
    (r'/permission_group_m2ms', auth.PermissionGroupM2MViewHandler),
    (r'/roles', auth.RoleViewHandler),
    (r'/user_roles', auth.UserRoleViewHandler),
    (r'/role_permissions', auth.RolePermissionViewHandler),
    (r'/role_permission_groups', auth.RolePermissionGroupViewHandler),
    (r'/user_permissions', auth.UserPermissionViewHandler),
    (r'/user_permission_groups', auth.UserPermissionGroupViewHandler),
    (r'/contenttypes', auth.ContentTypeViewHandler),
]
