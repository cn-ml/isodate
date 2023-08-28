"""
Collect all test suites into one TestSuite instance.
"""
from __future__ import annotations

import unittest
import warnings
from unittest import TestSuite

from isodate.tests import (
    test_date,
    test_time,
    test_datetime,
    test_duration,
    test_strf,
    test_pickle,
)


def test_suite() -> TestSuite:
    """
    Return a new TestSuite instance consisting of all available TestSuites.
    """
    warnings.filterwarnings("error", module=r"isodate(\..)*")

    return unittest.TestSuite(
        [
            test_date.test_suite(),
            test_time.test_suite(),
            test_datetime.test_suite(),
            test_duration.test_suite(),
            test_strf.test_suite(),
            test_pickle.test_suite(),
        ]
    )


if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")
