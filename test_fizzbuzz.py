# test_fizzbuzz.py
def test_fizzbuzz():
    from main import fizzbuzz # Import the fizzbuzz functon

    # Happy path (Fizz, Buzz, Fizzbuzz)
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"

    #Edge case (Not divisible by 3 or 5)
    assert fizzbuzz(7) == 7