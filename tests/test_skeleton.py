# -*- coding: utf-8 -*-

import pytest
from cube.skeleton import fib

__author__ = "Benno Schweikert"
__copyright__ = "Benno Schweikert"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
