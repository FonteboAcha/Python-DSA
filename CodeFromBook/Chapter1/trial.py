# alpha = [1, 2, 3]
# beta = alpha          # an alias for alpha
# beta += [4, 5]        # extends the original list with two more elements
# print(alpha)
# beta = beta + [6, 7]  # reassigns beta to a new list [1, 2, 3, 4, 5, 6, 7]
# print(beta )

# data = ["Achah", 2, 3, 4, 5]
#
# i = iter(data)    #create an iterator
#
# print(next(i))

# Comprehensions
# sum_squares = sum(k*k for k in range(7))
#
# print(sum_squares)

# packing of sequences
# data = 1, 2, 3, 4
#
# print(data)

# unpacking of sequences
# a, b, c, d = [1, 2, 3, 4]
#
# print(b, d, c, a)

import random
my_list = [num for num in range(random.randrange(0, 20))]

print(my_list)