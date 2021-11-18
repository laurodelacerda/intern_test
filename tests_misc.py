# -*- coding: utf-8 -*-
"""
author: Lauro de Lacerda
e-mail: lauro.lacerda@metaltoad.com

Please leave your Pytest unit tests here.
Give at least three unit test cases per method.
"""

import pytest
import misc

add = [(1, 1, 2),
       (0, 0, 0),
       (1, -2, -1)]
@pytest.mark.parametrize(["number1", "number2", "expected"], add)
def test_example_add(number1, number2, expected):
    assert misc.add(number1, number2) == expected

