from permission.models import Permission

ADD_USER = 'add_user'
DELETE_USER = 'delete_user'
CHANGE_USER = 'change_user'
VIEW_USER = 'view_user'

ADD_ROLE = 'add_role'
DELETE_ROLE = 'delete_role'
CHANGE_ROLE = 'change_role'
VIEW_ROLE = 'view_role'

ADD_ROLE_USER = 'add_role_user'
DELETE_ROLE_USER = 'delete_role_user'
CHANGE_ROLE_USER = 'change_role_user'
VIEW_ROLE_USER = 'view_role_user'


ADD_PERMISSION = 'add_permission'
DELETE_PERMISSION = 'delete_permission'
CHANGE_PERMISSION = 'change_permission'
VIEW_PERMISSION = 'view_permission'

ADD_PERMISSION_ROLE = 'add_permission_role'
DELETE_PERMISSION_ROLE = 'delete_permission_role'
CHANGE_PERMISSION_ROLE = 'change_permission_role'
VIEW_PERMISSION_ROLE = 'view_permission_role'

ADD_BOOK = 'add_book'
DELETE_BOOK = 'delete_book'
CHANGE_BOOK = 'change_book'
VIEW_BOOK = 'view_book'


PERMISSION_LIST = [
    {
        "key": ADD_USER,
        "value": 'can add user'
    },
    {
        "key": DELETE_USER,
        "value": 'can delete user'
    },
    {
        "key": VIEW_USER,
        "value": 'can view user'
    },
    {
        "key": CHANGE_USER,
        "value": 'can change user'
    },
    # Role
    {
        "key": ADD_ROLE,
        "value": 'can add role'
    },
    {
        "key": DELETE_ROLE,
        "value": 'can delete role'
    },
    {
        "key": VIEW_ROLE,
        "value": 'can view role'
    },
    {
        "key": CHANGE_ROLE,
        "value": 'can change role'
    },
    # RoleUser
    {
        "key": ADD_ROLE_USER,
        "value": 'can add role user'
    },
    {
        "key": DELETE_ROLE_USER,
        "value": 'can delete role user'
    },
    {
        "key": VIEW_ROLE_USER,
        "value": 'can view role user'
    },
    {
        "key": CHANGE_ROLE_USER,
        "value": 'can change role user'
    },

    # Permission
    {
        "key": ADD_PERMISSION,
        "value": 'can add permission'
    },
    {
        "key": DELETE_PERMISSION,
        "value": 'can delete permission'
    },
    {
        "key": VIEW_PERMISSION,
        "value": 'can view permission'
    },
    {
        "key": CHANGE_PERMISSION,
        "value": 'can change permission'
    },
    # Permission on Role
    {
        "key": ADD_PERMISSION_ROLE,
        "value": 'can add permission role'
    },
    {
        "key": DELETE_PERMISSION_ROLE,
        "value": 'can delete permission role'
    },
    {
        "key": VIEW_PERMISSION_ROLE,
        "value": 'can view permission role'
    },
    {
        "key": CHANGE_PERMISSION_ROLE,
        "value": 'can change permission role'
    },
    # Book
    {
        "key": ADD_PERMISSION_ROLE,
        "value": 'can add permission role'
    },
    {
        "key": DELETE_BOOK,
        "value": 'can delete book role'
    },
    {
        "key": VIEW_BOOK,
        "value": 'can view book role'
    },
    {
        "key": CHANGE_BOOK,
        "value": 'can change book role'
    },

]


def create_permissions():
    for p in PERMISSION_LIST:
        try:
            persmission = Permission.objects.create(**p)
            persmission.save()
        except Exception:
            pass
