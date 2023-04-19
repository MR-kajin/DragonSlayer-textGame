from project import check_name , class_choise, st_game
import unittest
import pytest
from game_classes import Knight, Wizard

def test_st_game():
    assert st_game("Play") == True
    assert st_game("Whatever") == False
    pytest.raises(SystemExit, st_game, "Quit")

def test_check_name():
    assert check_name("Kajin") == True
    assert check_name("MARCO RAFFAELE") == True
    assert check_name("areyouenjoyingplaythegame") == True
    assert check_name("kajin3833") == False
    assert check_name("best?A!") == False
    assert check_name("This isnt right") == False
    assert check_name("twentysixchrarenotallwowed") == False


class TestClass_Knight(unittest.TestCase):
    # test function to test whether obj is instance of class
    def test_positive(self):
        objectName = class_choise("black_dragon,","name","Knight")
        # error message in case if test case got failed
        message = "given object is not instance of Knight."
        # assertIsInstance() to check if obj is instance of class
        self.assertIsInstance(objectName, Knight, message)

    def test_negative(self):
        class_choise("black_dragon,","name","Marco") == False

class TestClass_Wizard(unittest.TestCase):
    # test function to test whether obj is instance of class
    def test_positive(self):
        objectName = class_choise("black_dragon,","name","Wizard")
        # error message in case if test case got failed
        message = "given object is not instance of Wizard."
        # assertIsInstance() to check if obj is instance of class
        self.assertIsInstance(objectName, Wizard, message)

    def test_negative(self):
        class_choise("black_dragon,","name","Marco") == False


if __name__ == '__main__':
    unittest.main()

