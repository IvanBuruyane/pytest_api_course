from datetime import datetime, timedelta

import pytest


@pytest.fixture
def time_tracker():
    tick = datetime.now()
    yield
    tock = datetime.now()
    diff = tock - tick
    print(f"\nruntime: {diff.total_seconds()}")
