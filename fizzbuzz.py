# For: fizzbuzz.py
# def generate(upto):
#     string = '1'
#     for n in range(2, upto + 1):
#         string = f'{string}, {n}'
#     return string

def fizzbuzz(upto):
    res = "1"
    for n in range(2, upto + 1):
        if n % 3 == 0 and n % 5 == 0:
            res = f'{res}, FizzBuzz'
        elif n % 3 == 0:
            res = f'{res}, Fizz'
        elif n % 5 == 0:
            res = f'{res}, Buzz'
        else:
            res = f'{res}, {n}'
    return res
