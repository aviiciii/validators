"""Test IBAN."""
# -*- coding: utf-8 -*-

# external
import pytest

# local
from validators import iban, ValidationFailure


@pytest.mark.parametrize("value", ["GB82WEST12345698765432", "NO9386011117947"])
def test_returns_true_on_valid_iban(value: str):
    """Test returns true on valid iban."""
    assert iban(value)


@pytest.mark.parametrize("value", ["GB81WEST12345698765432", "NO9186011117947"])
def test_returns_failed_validation_on_invalid_iban(value: str):
    """Test returns failed validation on invalid iban."""
    assert isinstance(iban(value), ValidationFailure)
