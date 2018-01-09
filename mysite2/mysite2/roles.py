from rolepermissions.roles import AbstractUserRole



class Manager(AbstractUserRole):
    available_permissions = {
    'create_users_record': True,
    }

class Staff(AbstractUserRole):
    available_permissions = {
    'edit_users_file': True,
    }


