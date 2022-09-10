from app.db.models import (ContentType, Permission, PermissionGroup,
                           PermissionGroupM2M, Role, RolePermission,
                           RolePermissionGroup, User, UserPermission,
                           UserPermissionGroup, UserRole)
from app.view.base import BaseViewHandler


class UserViewHandler(BaseViewHandler):
    """users

    Args:
        BaseViewHandler (_type_): _description_
    """

    def prepare(self):
        self.class_table = User


class PermissionViewHandler(BaseViewHandler):
    """permission

    Args:
        BaseViewHandler (_type_): _description_
    """

    def prepare(self):
        self.class_table = Permission


class PermissionGroupViewHandler(BaseViewHandler):
    """permission group

    Args:
        BaseViewHandler (_type_): _description_
    """

    def prepare(self):
        self.class_table = PermissionGroup


class PermissionGroupM2MViewHandler(BaseViewHandler):
    """permission group m2m

    Args:
        BaseViewHandler (_type_): _description_
    """

    def prepare(self):
        self.class_table = PermissionGroupM2M


class RoleViewHandler(BaseViewHandler):
    """role

    Args:
        BaseViewHandler (_type_): _description_
    """

    def prepare(self):
        self.class_table = Role


class UserRoleViewHandler(BaseViewHandler):
    """user role

    Args:
        BaseViewHandler (_type_): _description_
    """

    def prepare(self):
        self.class_table = UserRole


class RolePermissionViewHandler(BaseViewHandler):
    """role permission

    Args:
        BaseViewHandler (_type_): _description_
    """

    def prepare(self):
        self.class_table = RolePermission


class RolePermissionGroupViewHandler(BaseViewHandler):
    """role permission group

    Args:
        BaseViewHandler (_type_): _description_
    """

    def prepare(self):
        self.class_table = RolePermissionGroup


class UserPermissionViewHandler(BaseViewHandler):
    """user permission

    Args:
        BaseViewHandler (_type_): _description_
    """

    def prepare(self):
        self.class_table = UserPermission


class UserPermissionGroupViewHandler(BaseViewHandler):
    """user permission group

    Args:
        BaseViewHandler (_type_): _description_
    """

    def prepare(self):
        self.class_table = UserPermissionGroup


class ContentTypeViewHandler(BaseViewHandler):
    """models restful manage

    Args:
        BaseViewHandler (_type_): _description_
    """

    def prepare(self):
        self.class_table = ContentType
