from help_desk.departments import VALID_DEPARTMENTS

class Employee:
    next_id = 1

    VALID_ROLES = {"EMPLOYEE", "SUPPORT", "SUPERVISOR"}

    def __init__(self, name, department, role):

        if not isinstance(name, str):
            raise ValueError("Name must be a string")

        if not name.strip():
            raise ValueError("Name cannot be empty")

        if not isinstance(department, str):
            raise ValueError("Department must be a string")

        if not department.strip():
            raise ValueError("Department cannot be empty")

        if department not in VALID_DEPARTMENTS:
            raise ValueError(f"Invalid department: {department}")

        if not isinstance(role, str):
            raise ValueError("Role must be a string")

        if not role.strip():
            raise ValueError("Role cannot be empty")

        if role not in Employee.VALID_ROLES:
            raise ValueError(f"Invalid role: {role}")

        self.id = Employee.next_id
        Employee.next_id += 1

        self.name = name
        self.department = department
        self.role = role