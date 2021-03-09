import unittest
from main import calculate_food


class TestFoodFunction(unittest.TestCase):
    def testNoDogs(self):
        print("\nTest No Dogs")
        food_required = calculate_food(0, 0, 0, 100)
        assert food_required > 100

    def testNoFood(self):
        print("\nTest No Food")
        food_required = calculate_food(5, 5, 5, 0)
        assert food_required == 360

    def testMaxDogs(self):
        print("\nTest Max Dogs")
        food_required = calculate_food(10, 10, 10, 20)
        assert food_required == 696

    def testMaxFood(self):
        print("\nTest Max Food")
        food_required = calculate_food(0, 0, 30, 0)
        assert food_required == 1080

    def testMinFoodMaxDogs(self):
        print("\nTest Minimum Food with Maximum Dogs")
        food_required = calculate_food(30, 0, 0, 300)
        assert food_required == 60

    def testMinFoodMinDogs(self):
        print("\nTest Minimum Food with Minimum Dogs")
        food_required = calculate_food(1, 0, 0, 11)
        assert food_required == 1.2

    def testFoodRequiredTwoDecimals(self):
        print("\nTest Food Required Returned to the hundredths")
        food_required = calculate_food(5, 3, 7, .01)
        assert food_required == 383.99

    def testNoFoodRequired(self):
        print("\nTest No Food Required")
        food_required = calculate_food(3, 2, 4, 300)
        assert food_required == 0

    def testTooManyDogs(self):
        print("\nTest More than Max Number of Dogs")
        error = calculate_food(10, 11, 10, 400)
        assert error == "Only 30 dogs allowed in the shelter at one time"

    def testNegativeDogs(self):
        print("\nTest Amount of Dogs given as negative number")
        error = calculate_food(10, -1, 10, 20)
        assert error == "Cannot have a negative amount of dogs"

    def testNegativeFood(self):
        print("\nTest Amount of Food given as negative number")
        error = calculate_food(10, 1, 10, -20)
        assert error == "Cannot have a negative amount of food"

    def testNormalFunction(self):
        print("\nTest for Normal Function or Happy Path")
        food_required = calculate_food(5, 3, 7, 17)
        assert food_required == 363.6


if __name__ == "__main__":
    unittest.main()  # run all tests
