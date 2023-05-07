from functions import pull_fortune, wish_block, prayer_box, final_fortune, entrance
import pytest
import builtins

def test_prayer_box(monkeypatch):
    inputs = iter(['y', 'y', ' ', 'Quit'])
    monkeypatch.setattr('builtins.input', lambda _="": next(inputs))
    prayer_box()

    