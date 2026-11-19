import pytest

from library_fines import can_borrow, late_fine, renewal_status


@pytest.mark.parametrize(
    ("member", "days", "damaged", "expected"),
    [
        ("student", 10, False, 0),
        ("guest", 15, False, 5),
        ("faculty", 31, False, 1),
        ("student", 115, True, 350),
    ],
)
def test_late_fines(member, days, damaged, expected):
    assert late_fine(member, days, damaged) == expected


@pytest.mark.parametrize(
    ("member", "days", "message"),
    [("alumni", 10, "unknown member"), ("student", -1, "invalid days")],
)
def test_invalid_loans(member, days, message):
    with pytest.raises(ValueError, match=message):
        late_fine(member, days, False)


@pytest.mark.parametrize(
    ("books", "fine", "member", "expected"),
    [
        (1, 0, "student", True),
        (1, 101, "student", False),
        (9, 100, "faculty", True),
    ],
)
def test_borrowing(books, fine, member, expected):
    assert can_borrow(books, fine, member) is expected


@pytest.mark.parametrize(
    ("renewals", "reserved", "days_left", "expected"),
    [
        (0, True, 5, "denied"),
        (2, False, 5, "limit reached"),
        (1, False, -1, "overdue"),
        (1, False, 0, "renewed"),
    ],
)
def test_renewals(renewals, reserved, days_left, expected):
    assert renewal_status(renewals, reserved, days_left) == expected
