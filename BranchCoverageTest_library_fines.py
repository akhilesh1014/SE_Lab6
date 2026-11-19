import pytest

from library_fines import can_borrow, late_fine, renewal_status


@pytest.mark.parametrize(
    ("member", "days", "damaged", "expected"),
    [
        ("student", 14, False, 0),
        ("student", 14, True, 150),
        ("student", 15, False, 2),
        ("faculty", 30, False, 0),
        ("faculty", 31, True, 151),
        ("guest", 54, False, 200),
        ("guest", 55, False, 200),
        ("guest", 55, True, 350),
    ],
)
def test_fine_decisions_at_boundaries(member, days, damaged, expected):
    assert late_fine(member, days, damaged) == expected


@pytest.mark.parametrize(
    ("member", "days", "message"),
    [("alumni", 0, "unknown member"), ("faculty", -1, "invalid days")],
)
def test_invalid_loan_decisions(member, days, message):
    with pytest.raises(ValueError, match=message):
        late_fine(member, days, False)


@pytest.mark.parametrize(
    ("books", "fine", "member", "expected"),
    [
        (2, 100, "student", True),
        (3, 100, "student", False),
        (9, 100, "faculty", True),
        (10, 100, "faculty", False),
        (0, 101, "faculty", False),
    ],
)
def test_borrowing_decisions_at_limits(books, fine, member, expected):
    assert can_borrow(books, fine, member) is expected


@pytest.mark.parametrize(
    ("renewals", "reserved", "days_left", "expected"),
    [
        (2, True, -1, "denied"),
        (2, False, -1, "limit reached"),
        (1, False, -1, "overdue"),
        (1, False, 0, "renewed"),
    ],
)
def test_renewal_precedence_and_boundaries(
    renewals, reserved, days_left, expected
):
    assert renewal_status(renewals, reserved, days_left) == expected
