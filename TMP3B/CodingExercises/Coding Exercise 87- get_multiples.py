'''
evens = get_multiples(2, 3)
next(evens) # 2
next(evens) # 4
next(evens) # 6
next(evens) # StopIteration

default_multiples = get_multiples()
list(default_multiples) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''


def get_multiples(number=1, count=10):
    multiplier = 1
    while multiplier <= count:
        yield number * multiplier
        multiplier += 1

# alt instructor solve
#     next_num = num
#     while count > 0:
#         yield next_num
#         count -= 1
#         next_num += num
