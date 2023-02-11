# import functions
#
# print(functions.multiply(5, 6))
from functions import multiply
from functions import no_of_letter
def test_multiply():
    assert multiply(5, 10) == 50
    assert multiply(100, 1.1) == 110
    assert multiply(1.5, 1.5) == 2.25
    assert multiply(3, 'mama') == 'mamamamamama'
    #assert multiply(None, 5) == None

def test_number_of_letters():
    assert no_of_letter('mama') == 4
    assert no_of_letter('mama.tata') == 8