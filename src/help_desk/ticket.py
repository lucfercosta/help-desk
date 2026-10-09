from datetime import datetime
from help_desk.departments import VALID_DEPARTMENTS
from help_desk.employee import Employee


class Ticket:

    next_id = 1
    VALID_CATEGORIES = {"HARDWARE", "SOFTWARE", "NETWORK", "ACCESS", "OTHER"}
    VALID_PRIORITIES = {"LOW", "MEDIUM", "HIGH", "CRITICAL"}
    VALID_STATUSES = {"OPEN", "IN_PROGRESS", "RESOLVED", "CLOSED"}
    ALLOWED_TRANSITIONS = {"OPEN": {"IN_PROGRESS"}, "IN_PROGRESS": {"RESOLVED"}, "RESOLVED": {"CLOSED"}}

    def __init__(self, title, description, category, department, priority, submitted_by):

        if not isinstance(title, str):
            raise ValueError("Title must be a string")

        if not title.strip():
            raise ValueError("Title cannot be empty")

        if not isinstance(description, str):
            raise ValueError("Description must be a string")

        if not description.strip():
            raise ValueError("Description cannot be empty")

        if category not in Ticket.VALID_CATEGORIES:
            raise ValueError(f"Invalid category: {category}")

        if priority not in Ticket.VALID_PRIORITIES:
            raise ValueError(f"Invalid priority: {priority}")

        if department not in VALID_DEPARTMENTS:
            raise ValueError(f"Invalid department: {department}")

        self.id = Ticket.next_id
        Ticket.next_id += 1

        self.title = title
        self.description = description
        self.priority = priority
        self.submitted_by = submitted_by
        self.assigned_to = None
        self.category = category
        self.department = department

        self.status = "OPEN"

        now = datetime.now()
        self.created_at = now
        self.updated_at = now
        self.resolved_at = None


    def change_status(self, new_status):

        if new_status not in self.VALID_STATUSES:
            raise ValueError(f"Invalid status: {new_status}")

        if new_status not in self.ALLOWED_TRANSITIONS.get(self.status, set()):
            raise ValueError(f"Cannot change from {self.status} to {new_status}")

        now = datetime.now()

        if new_status == "RESOLVED":
            self.resolved_at = now
       
        self.status = new_status
        self.updated_at = now


    def change_priority(self, new_priority):
        if new_priority not in self.VALID_PRIORITIES:
            raise ValueError(f"Invalid priority {new_priority}")

        now = datetime.now()
        self.priority = new_priority
        self.updated_at = now


    def assign_to(self, employee):
        if not isinstance(employee, Employee):
            raise ValueError("Employee must be an Employee object")

        if employee.role != "SUPPORT":
            raise ValueError("Only support employees can be assigned tickets")

        if employee.department != self.department:
            raise ValueError("Employee and ticket departments must match")

        self.assigned_to = employee