
from ticket import Ticket
from datetime import datetime


def test_resolved_at_on_creation():
    ticket = Ticket(
        title="Computer won't start",
        description="The computer does not turn on.",
        category="HARDWARE",
        department="IT",
        priority="HIGH",
        submitted_by="Lucas",
    )

    assert ticket.resolved_at is None


def test_resolved_at_before_resolution():
    ticket = Ticket(
        title="Computer won't start",
        description="The computer does not turn on.",
        category="HARDWARE",
        department="IT",
        priority="HIGH",
        submitted_by="Lucas",
    )

    ticket.change_status("IN_PROGRESS")

    assert ticket.resolved_at is None


def test_resolved_at_after_resolution():
    ticket = Ticket(
        title="Computer won't start",
        description="The computer does not turn on.",
        category="HARDWARE",
        department="IT",
        priority="HIGH",
        submitted_by="Lucas",
    )

    ticket.change_status("IN_PROGRESS")
    ticket.change_status("RESOLVED")

    assert isinstance(ticket.resolved_at, datetime)
    assert ticket.updated_at == ticket.resolved_at


def test_change_priority():
    ticket = Ticket(
        title="Computer issue",
        description="Computer won't start",
        category="HARDWARE",
        department="IT",
        priority="LOW",
        submitted_by="Lucas",
    )

    old_updated_at = ticket.updated_at

    ticket.change_priority("HIGH")

    assert ticket.priority == "HIGH"
    assert ticket.updated_at >= old_updated_at


def test_invalid_priority_does_not_change_ticket():
    ticket = Ticket(
        title="Computer issue",
        description="Computer won't start",
        category="HARDWARE",
        department="IT",
        priority="LOW",
        submitted_by="Lucas",
    )

    old_updated_at = ticket.updated_at

    try:
        ticket.change_priority("URGENT")
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for invalid priority")

    assert ticket.priority == "LOW"
    assert ticket.updated_at == old_updated_at


def test_empty_title_is_rejected():
    try:
        Ticket(
            title="",
            description="The computer does not turn on.",
            category="HARDWARE",
            department="IT",
            priority="HIGH",
            submitted_by="Lucas",
        )
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for empty title")


def test_whitespace_title_is_rejected():
    try:
        Ticket(
            title="   ",
            description="The computer does not turn on.",
            category="HARDWARE",
            department="IT",
            priority="HIGH",
            submitted_by="Lucas",
        )
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for whitespace-only title")


def test_whitespace_description_is_rejected():
    try:
        Ticket(
            title="Computer won't start",
            description="   ",
            category="HARDWARE",
            department="IT",
            priority="HIGH",
            submitted_by="Lucas",
        )
    except ValueError:
        pass
    else:
        raise AssertionError(
            "Expected ValueError for whitespace-only description"
        )


def test_valid_category():
    ticket = Ticket(
        title="Computer won't start",
        description="The computer does not turn on.",
        category="HARDWARE",
        department="IT",
        priority="HIGH",
        submitted_by="Lucas",
    )

    assert ticket.category == "HARDWARE"


def test_invalid_category_is_rejected():
    try:
        Ticket(
            title="Computer won't start",
            description="The computer does not turn on.",
            category="PRINTER",
            department="IT",
            priority="HIGH",
            submitted_by="Lucas",
        )
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for invalid category")


def test_valid_department():
    ticket = Ticket(
        title="Payroll issue",
        description="Cannot access payroll software.",
        category="SOFTWARE",
        department="FINANCE",
        priority="MEDIUM",
        submitted_by="Lucas",
    )

    assert ticket.department == "FINANCE"


def test_invalid_department_is_rejected():
    try:
        Ticket(
            title="Payroll issue",
            description="Cannot access payroll software.",
            category="SOFTWARE",
            department="MARKETING",
            priority="MEDIUM",
            submitted_by="Lucas",
        )
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for invalid department")


def test_valid_status_transition():
    ticket = Ticket(
        title="Computer won't start",
        description="The computer does not turn on.",
        category="HARDWARE",
        department="IT",
        priority="HIGH",
        submitted_by="Lucas",
    )

    ticket.change_status("IN_PROGRESS")

    assert ticket.status == "IN_PROGRESS"

def test_invalid_status_transition_is_rejected():
    ticket = Ticket(
        title="Computer won't start",
        description="The computer does not turn on.",
        category="HARDWARE",
        department="IT",
        priority="HIGH",
        submitted_by="Lucas",
    )

    try:
        ticket.change_status("RESOLVED")
    except ValueError:
        pass
    else:
        raise AssertionError(
            "Expected ValueError for invalid status transition"
        )

    assert ticket.status == "OPEN"


def test_updated_at_changes_when_status_changes():
    ticket = Ticket(
        title="Computer won't start",
        description="The computer does not turn on.",
        category="HARDWARE",
        department="IT",
        priority="HIGH",
        submitted_by="Lucas",
    )

    old_updated_at = ticket.updated_at

    ticket.change_status("IN_PROGRESS")

    assert ticket.updated_at >= old_updated_at


def test_complete_status_workflow():
    ticket = Ticket(
        title="Computer won't start",
        description="The computer does not turn on.",
        category="HARDWARE",
        department="IT",
        priority="HIGH",
        submitted_by="Lucas",
    )

    ticket.change_status("IN_PROGRESS")
    assert ticket.status == "IN_PROGRESS"

    ticket.change_status("RESOLVED")
    assert ticket.status == "RESOLVED"
    assert ticket.resolved_at is not None

    ticket.change_status("CLOSED")
    assert ticket.status == "CLOSED"


def test_invalid_ticket_does_not_consume_id():
    next_id_before = Ticket.next_id

    try:
        Ticket(
            title="Computer issue",
            description="Computer won't start.",
            category="HARDWARE",
            department="INVALID",
            priority="HIGH",
            submitted_by="Lucas",
        )
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for invalid department")

    assert Ticket.next_id == next_id_before


def test_invalid_status_transition_does_not_change_updated_at():
    ticket = Ticket(
        title="Computer won't start",
        description="The computer does not turn on.",
        category="HARDWARE",
        department="IT",
        priority="HIGH",
        submitted_by="Lucas",
    )

    old_updated_at = ticket.updated_at

    try:
        ticket.change_status("RESOLVED")
    except ValueError:
        pass
    else:
        raise AssertionError(
            "Expected ValueError for invalid status transition"
        )

    assert ticket.status == "OPEN"
    assert ticket.updated_at == old_updated_at

# Run all tests
test_resolved_at_on_creation()
test_resolved_at_before_resolution()
test_resolved_at_after_resolution()
test_change_priority()
test_invalid_priority_does_not_change_ticket()
test_empty_title_is_rejected()
test_whitespace_title_is_rejected()
test_whitespace_description_is_rejected()
test_valid_category()
test_invalid_category_is_rejected()
test_valid_department()
test_invalid_department_is_rejected()
test_valid_status_transition()
test_invalid_status_transition_is_rejected()
test_updated_at_changes_when_status_changes()
test_complete_status_workflow()
test_invalid_ticket_does_not_consume_id()
test_invalid_status_transition_does_not_change_updated_at()

print("All tests passed!")