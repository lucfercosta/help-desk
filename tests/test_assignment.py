import pytest
from help_desk.employee import Employee
from help_desk.ticket import Ticket


def test_support_employee_can_be_assigned_to_ticket():
    # Arrange: create the employee and ticket.
    employee = Employee(
        name="Alex Smith",
        department="IT",
        role="SUPPORT",
    )

    ticket = Ticket(
        title="Computer won't start",
        description="The computer does not turn on.",
        category="HARDWARE",
        department="IT",
        priority="HIGH",
        submitted_by="Maria Silva",
    )

    # Act: assign the employee to the ticket.
    ticket.assign_to(employee)

    # Assert: verify that the correct employee was assigned.
    assert ticket.assigned_to is employee


def test_non_support_employee_cannot_be_assigned_to_ticket():
    employee = Employee(
        name="Maria Silva",
        department="IT",
        role="EMPLOYEE",
    )

    ticket = Ticket(
        title="Computer won't start",
        description="The computer does not turn on.",
        category="HARDWARE",
        department="IT",
        priority="HIGH",
        submitted_by="Alex Smith",
    )

    with pytest.raises(ValueError):
        ticket.assign_to(employee)

    assert ticket.assigned_to is None


def test_employee_from_different_department_cannot_be_assigned():
    employee = Employee(
        name="Maria Silva",
        department="HR",
        role="SUPPORT",
    )

    ticket = Ticket(
        title="Computer won't start",
        description="The computer does not turn on.",
        category="HARDWARE",
        department="IT",
        priority="HIGH",
        submitted_by="Alex Smith",
    )

    with pytest.raises(ValueError):
        ticket.assign_to(employee)

    assert ticket.assigned_to is None


def test_invalid_object_cannot_be_assigned_to_ticket():
    ticket = Ticket(
        title="Computer won't start",
        description="The computer does not turn on.",
        category="HARDWARE",
        department="IT",
        priority="HIGH",
        submitted_by="Maria Silva",
    )

    with pytest.raises(ValueError):
        ticket.assign_to("Alex Smith")

    assert ticket.assigned_to is None