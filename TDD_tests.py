# # import functions
# #
# # print(functions.multiply(5, 6))
# from functions import multiply
# from functions import no_of_letter
# def test_multiply():
#     assert multiply(5, 10) == 50
#     assert multiply(100, 1.1) == 110
#     assert multiply(1.5, 1.5) == 2.25
#     assert multiply(3, 'mama') == 'mamamamamama'
#     #assert multiply(None, 5) == None
#
# def test_number_of_letters():
#     assert no_of_letter('mama') == 4
#     assert no_of_letter('mama.tata') == 8

from functions import fizz_buzz

def test_fizz_buzz():
    assert fizz_buzz(15) == 'FizzBuzz'
    assert fizz_buzz(10) == 'Buzz'
    assert fizz_buzz(9) == 'Fizz'
    assert fizz_buzz(8) == 8

def test_fizzbuzz_advanced():
    assert fizz_buzz(1.3) == 1
    assert fizz_buzz(1.9) == 1
    assert fizz_buzz('1') == 1
    assert fizz_buzz('1.7') == 1
    assert fizz_buzz(5.9) == 'Buzz'
    assert fizz_buzz('5.9') == 'Buzz'
    assert fizz_buzz(0) == None
    assert fizz_buzz('mama') == None

