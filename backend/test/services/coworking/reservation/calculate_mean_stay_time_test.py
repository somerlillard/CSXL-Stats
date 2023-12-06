"""ReservationService#calculate_mean_stay_time tests."""

from unittest.mock import create_autospec, call

import pandas as pd

from backend.models.coworking.reservation import ReservationState

from .....services.coworking import ReservationService
from .....services import PermissionService
from .....models.coworking import Reservation
from .....services.exceptions import ResourceNotFoundException, UserPermissionException

# Imported fixtures provide dependencies injected for the tests as parameters.
# Dependent fixtures (seat_svc) are required to be imported in the testing module.
from ..fixtures import (
    reservation_svc,
    permission_svc,
    seat_svc,
    policy_svc,
    operating_hours_svc,
)
from ..time import *

# Import the setup_teardown fixture explicitly to load entities in database.
# The order in which these fixtures run is dependent on their imported alias.
# Since there are relationship dependencies between the entities, order matters.
from ...core_data import setup_insert_data_fixture as insert_order_0
from ..operating_hours_data import fake_data_fixture as insert_order_1
from ..room_data import fake_data_fixture as insert_order_2
from ..seat_data import fake_data_fixture as insert_order_3
from .reservation_data import fake_data_fixture as insert_order_4

# Import the fake model data in a namespace for test assertions
from ...core_data import user_data
from .. import seat_data
from . import reservation_data


def test_calculate_mean_stay_time_for_day(reservation_svc: ReservationService):
    """Revised test to cover individual dates and edge cases."""
    end_date = datetime.now()
    time_range = "day"

    mean_stay = reservation_svc.calculate_mean_stay_time(user_data.user, time_range)

    start_date = reservation_svc._get_start_date_for_time_range(end_date, time_range)

    reservations = [
        reservation
        for reservation in reservation_data.reservations
        if (
            reservation.users == [user_data.user]
            and ReservationState.CHECKED_OUT in reservation.state
            and reservation.start >= start_date
            and reservation.end <= end_date
        )
    ]

    if not reservations:
        assert mean_stay == 0
        return

    total_time = sum([(res.end - res.start).total_seconds() for res in reservations])
    mean_time = total_time / len(reservations)
    expect_mean_stay = mean_time / 60

    assert mean_stay == expect_mean_stay


def test_calculate_mean_stay_time_for_week(reservation_svc: ReservationService):
    """Revised test to cover individual dates and edge cases."""
    end_date = datetime.now()
    time_range = "week"

    mean_stay = reservation_svc.calculate_mean_stay_time(user_data.user, time_range)

    start_date = reservation_svc._get_start_date_for_time_range(end_date, time_range)

    reservations = [
        reservation
        for reservation in reservation_data.reservations
        if (
            reservation.users == [user_data.user]
            and ReservationState.CHECKED_OUT in reservation.state
            and reservation.start >= start_date
            and reservation.end <= end_date
        )
    ]

    if not reservations:
        assert mean_stay == 0
        return

    total_time = sum([(res.end - res.start).total_seconds() for res in reservations])
    mean_time = total_time / len(reservations)
    expect_mean_stay = mean_time / 60

    assert mean_stay == expect_mean_stay


def test_calculate_mean_stay_time_for_month(reservation_svc: ReservationService):
    """Revised test to cover individual dates and edge cases."""
    end_date = datetime.now()
    time_range = "month"

    mean_stay = reservation_svc.calculate_mean_stay_time(user_data.user, time_range)

    start_date = reservation_svc._get_start_date_for_time_range(end_date, time_range)

    reservations = [
        reservation
        for reservation in reservation_data.reservations
        if (
            reservation.users == [user_data.user]
            and ReservationState.CHECKED_OUT in reservation.state
            and reservation.start >= start_date
            and reservation.end <= end_date
        )
    ]

    if not reservations:
        assert mean_stay == 0
        return

    total_time = sum([(res.end - res.start).total_seconds() for res in reservations])
    mean_time = total_time / len(reservations)
    expect_mean_stay = mean_time / 60

    assert mean_stay == expect_mean_stay


def test_calculate_mean_stay_time_for_year(reservation_svc: ReservationService):
    """Revised test to cover individual dates and edge cases."""
    end_date = datetime.now()
    time_range = "year"

    mean_stay = reservation_svc.calculate_mean_stay_time(user_data.user, time_range)

    start_date = reservation_svc._get_start_date_for_time_range(end_date, time_range)

    reservations = [
        reservation
        for reservation in reservation_data.reservations
        if (
            reservation.users == [user_data.user]
            and ReservationState.CHECKED_OUT in reservation.state
            and reservation.start >= start_date
            and reservation.end <= end_date
        )
    ]

    if not reservations:
        assert mean_stay == 0
        return

    total_time = sum([(res.end - res.start).total_seconds() for res in reservations])
    mean_time = total_time / len(reservations)
    expect_mean_stay = mean_time / 60

    assert mean_stay == expect_mean_stay