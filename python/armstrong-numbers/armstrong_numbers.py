def is_armstrong(number):
    return True if sum([int(x) ** len(str(number))  for x in str(number)]) == number else False

