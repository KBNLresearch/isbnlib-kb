# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""nose tests for metadata."""

from nose.tools import assert_equals
from isbnlib import meta
from .._kb import query


def test_query():
    """Test the query of metadata (LoC Library of Congress) with 'low level' queries."""
    assert_equals(len(repr(query('9789045040110'))) > 100, True)
    print(repr(query('9021615258')))
    print(len(repr(query('9021615258'))))
    assert_equals(len(repr(query('9021615258'))) > 100, True)


def test_query_missing():
    """Test LoC with 'low level' queries (missing data)."""
    assert_equals(len(repr(query('9781849692341'))) <= 2, True)
    assert_equals(len(repr(query('9781849692343'))) <= 2, True)


def test_query_wrong():
    """Test LoC with 'low level' queries (wrong data)."""
    assert_equals(len(repr(query('9780000000'))) <= 2, True)
