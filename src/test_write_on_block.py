from functions import wish_block
import builtins
import pytest 
import csv

# This test checks whether the application can create and write to a csv file.
# It opens and creates a csv file with the entry "22/03,My First Wish"
# The test then checks whether that file was created and if the first line matches the string.

def test_wish_block(monkeypatch):
    with pytest.raises(KeyboardInterrupt):
        inputs = iter(['Wish', 'My First Wish', '22/03', 'Leave', 'Quit'])
        monkeypatch.setattr('builtins.input', lambda _="": next(inputs))
        wish_block()
    with open('mywishes.csv', "r") as file:
        reader = csv.reader(file)
        firstline = file.readline()
        assert firstline == "22/03,My First Wish\n"
