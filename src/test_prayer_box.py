from functions import prayer_box
import pytest
import builtins

# This test checks whether the user can make it from the prayer_box function
# to the end of the program.
# Once a user types Quit, the application raises a Keyboard Interrupt,
# this test checks whether the user can make it to that point.

def test_prayer_box(monkeypatch):
    with pytest.raises(KeyboardInterrupt):
        inputs = iter(['y', 'y', ' ', 'Quit'])
        monkeypatch.setattr('builtins.input', lambda _="": next(inputs))
        prayer_box()
    with pytest.raises(KeyboardInterrupt):
        inputs = iter(['y', 'n', 'Quit'])
        monkeypatch.setattr('builtins.input', lambda _="": next(inputs))
        prayer_box()


