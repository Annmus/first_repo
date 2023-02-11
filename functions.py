# def multiply(x, y):
#     if isinstance(x, (int, float)) and isinstance(y, (int, float)):
#         return round(x * y, 5)
#     else:
#         return x * y
#
# def no_of_letter(text):
#     return len(text)

def fizz_buzz(x):
    try:
        x = int(float(x))
        if isinstance(x, (int, float)) and x >= 1:
            if x % 3 == 0 and x % 5 == 0:
                return 'FizzBuzz'
            elif x % 3 == 0:
                return 'Fizz'
            elif x % 5 == 0:
                return 'Buzz'
            else:
                return x
        else:
            return None
    except:
        return None



