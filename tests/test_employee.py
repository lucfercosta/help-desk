import pytest
from help_desk.employee import Employee


def test_valid_employee():
    employee = Employee(
        name="Alex Smith",
        department="IT",
        role="SUPPORT",
    )

    assert employee.id > 0
    assert employee.name == "Alex Smith"
    assert employee.department == "IT"
    assert employee.role == "SUPPORT"


def test_invalid_department_is_rejected():
    with pytest.raises(ValueError):
        Employee(
            name="Alex Smith",
            department="MARKETING",
            role="SUPPORT",
        )


def test_invalid_role_is_rejected():
    with pytest.raises(ValueError):
        Employee(
            name="Alex Smith",
            department="IT",
            role="MANAGER",
        )


def test_invalid_employee_does_not_consume_id():
    starting_id = Employee.next_id

    with pytest.raises(ValueError):
        Employee(
            name="Alex Smith",
            department="MARKETING",
            role="SUPPORT",
        )

    assert Employee.next_id == starting_id


def test_empty_name_is_rejected():
    with pytest.raises(ValueError):
        Employee(
            name="   ",
            department="IT",
            role="SUPPORT",
        )


def test_empty_department_is_rejected():
    with pytest.raises(ValueError):
        Employee(
            name="Alex Smith",
            department="   ",
            role="SUPPORT",
        )


def test_empty_role_is_rejected():
    with pytest.raises(ValueError):
        Employee(
            name="Alex Smith",
            department="IT",
            role="   ",
        )


def test_employees_receive_unique_ids():
    first = Employee(
        name="Alex Smith",
        department="IT",
        role="SUPPORT",
    )

    second = Employee(
        name="Maria Silva",
        department="HR",
        role="EMPLOYEE",
    )

    assert second.id == first.id + 1
    assert first.id != second.id


def test_non_string_name_is_rejected():
    with pytest.raises(ValueError):
        Employee(
            name=None,
            department="IT",
            role="SUPPORT",
        )


def test_non_string_department_is_rejected():
    with pytest.raises(ValueError):
        Employee(
            name="Alex Smith",
            department=None,
            role="SUPPORT",
        )


def test_non_string_role_is_rejected():
    with pytest.raises(ValueError):
        Employee(
            name="Alex Smith",
            department="IT",
            role=None,
        )


def test_non_string_name_does_not_consume_id():
    starting_id = Employee.next_id

    with pytest.raises(ValueError):
        Employee(
            name=None,
            department="IT",
            role="SUPPORT",
        )

    assert Employee.next_id == starting_id