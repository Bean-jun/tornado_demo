import datetime

from sqlalchemy import String, Column, DateTime, BigInteger
from sqlalchemy.dialects.mysql import LONGTEXT

from app.db import Base


class User(Base):

    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment='用户')
    username = Column(String(512, 'utf8mb4_general_ci'), nullable=False, comment='名称')
    realname = Column(String(512, 'utf8mb4_general_ci'), server_default="", comment='真实姓名')
    password = Column(String(1024, 'utf8mb4_general_ci'), nullable=False, comment='密码')
    gender = Column(String(512, 'utf8mb4_general_ci'), server_default="保密", comment='性别')
    login_time = Column(DateTime, comment='登录时间')
    pwd_change_time = Column(DateTime, comment='密码修改时间')
    face = Column(String(512, 'utf8mb4_general_ci'), server_default="", comment='头像')
    errnum = Column(BigInteger, server_default="0", comment='登录错误次数')
    errtime = Column(DateTime, comment='登录错误时间')
    createtime = Column(DateTime, default=datetime.datetime.now, comment="创建时间")
    modifiedtime = Column(DateTime, default=datetime.datetime.now, comment="修改时间")
    state = Column(BigInteger, server_default="1", comment='状态')


class Permission(Base):

    __tablename__ = "permissions"

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment="权限表")
    name = Column(String(1024), nullable=False, comment='名称')
    codename = Column(String(1024), server_default="", comment='别名')
    contenttypeid = Column(BigInteger, nullable=False, comment='类型id')
    method = Column(String(1024), server_default="", comment='请求方法')
    createtime = Column(DateTime, default=datetime.datetime.now, comment="创建时间")
    modifiedtime = Column(DateTime, default=datetime.datetime.now, comment="修改时间")
    remark = Column(String(1024), server_default="", comment='备注')
    state = Column(BigInteger, server_default="1", comment='状态')


class PermissionGroup(Base):

    __tablename__ = "permission_groups"

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment="权限组表")
    name = Column(String(1024), nullable=False, comment='名称')
    createtime = Column(DateTime, default=datetime.datetime.now, comment="创建时间")
    modifiedtime = Column(DateTime, default=datetime.datetime.now, comment="修改时间")
    remark = Column(String(1024), server_default="", comment='备注')
    state = Column(BigInteger, server_default="1", comment='状态')


class PermissionGroupM2M(Base):

    __tablename__ = "permission_group_m2ms"

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment="权限组权限表")
    permissiongroupid = Column(BigInteger, nullable=False, comment='权限组')
    permissionid = Column(BigInteger, nullable=False, comment='权限')
    createtime = Column(DateTime, default=datetime.datetime.now, comment="创建时间")
    modifiedtime = Column(DateTime, default=datetime.datetime.now, comment="修改时间")
    remark = Column(String(1024), server_default="", comment='备注')
    state = Column(BigInteger, server_default="1", comment='状态')


class Role(Base):
    
    __tablename__ = 'roles'

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment='角色')
    name = Column(String(1024, 'utf8mb4_general_ci'), nullable=False, comment='名称')
    langname = Column(String(1024, 'utf8mb4_general_ci'), server_default="", comment='别名')
    level = Column(BigInteger, nullable=False, comment='等级')
    createtime = Column(DateTime, default=datetime.datetime.now, comment="创建时间")
    modifiedtime = Column(DateTime, default=datetime.datetime.now, comment="修改时间")
    remark = Column(String(1024), server_default="", comment='备注')
    state = Column(BigInteger, server_default="1", comment='状态')


class UserRole(Base):

    __tablename__ = "user_roles"

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment="用户角色表")
    userid = Column(BigInteger, nullable=False, comment='用户id')
    roleid = Column(BigInteger, nullable=False, comment='角色id')
    createtime = Column(DateTime, default=datetime.datetime.now, comment="创建时间")
    modifiedtime = Column(DateTime, default=datetime.datetime.now, comment="修改时间")
    remark = Column(String(1024), server_default="", comment='备注')
    state = Column(BigInteger, server_default="1", comment='状态')


class RolePermission(Base):

    __tablename__ = "role_permissions"

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment="角色权限表")
    permissionid = Column(BigInteger, nullable=False, comment='权限id')
    roleid = Column(BigInteger, nullable=False, comment='角色id')
    createtime = Column(DateTime, default=datetime.datetime.now, comment="创建时间")
    modifiedtime = Column(DateTime, default=datetime.datetime.now, comment="修改时间")
    remark = Column(String(1024), server_default="", comment='备注')
    state = Column(BigInteger, server_default="1", comment='状态')


class RolePermissionGroup(Base):

    __tablename__ = "role_permission_groups"

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment="角色权限组表")
    permissiongroupid = Column(BigInteger, nullable=False, comment='权限组id')
    roleid = Column(BigInteger, nullable=False, comment='角色id')
    createtime = Column(DateTime, default=datetime.datetime.now, comment="创建时间")
    modifiedtime = Column(DateTime, default=datetime.datetime.now, comment="修改时间")
    remark = Column(String(1024), server_default="", comment='备注')
    state = Column(BigInteger, server_default="1", comment='状态')


class UserPermission(Base):

    __tablename__ = "user_permissions"

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment="用户权限表")
    userid = Column(BigInteger, nullable=False, comment='用户id')
    permissionid = Column(BigInteger, nullable=False, comment='权限id')
    createtime = Column(DateTime, default=datetime.datetime.now, comment="创建时间")
    modifiedtime = Column(DateTime, default=datetime.datetime.now, comment="修改时间")
    remark = Column(String(1024), server_default="", comment='备注')
    state = Column(BigInteger, server_default="1", comment='状态')


class UserPermissionGroup(Base):

    __tablename__ = "user_permission_groups"

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment="用户权限组表")
    userid = Column(BigInteger, nullable=False, comment='用户id')
    permissiongroupid = Column(BigInteger, nullable=False, comment='权限组id')
    createtime = Column(DateTime, default=datetime.datetime.now, comment="创建时间")
    modifiedtime = Column(DateTime, default=datetime.datetime.now, comment="修改时间")
    remark = Column(String(1024), server_default="", comment='备注')
    state = Column(BigInteger, server_default="1", comment='状态')


class ContentType(Base):

    __tablename__ = "contenttypes"

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment="模型内容表")
    name = Column(String(1024), comment='表名')
    model = Column(String(1024), comment='模型')
    createtime = Column(DateTime, default=datetime.datetime.now, comment="创建时间")
    modifiedtime = Column(DateTime, default=datetime.datetime.now, comment="修改时间")
    remark = Column(String(1024), server_default="", comment='备注')
    state = Column(BigInteger, server_default="1", comment='状态')
