# Write a lambda expression that has two numeric parameters. If the second argument equals zero, it should return
# None. Otherwise, it should return the value of dividing the first argument by the second argument.

print((lambda x1, x2: None if x2 == 0 else x1 / x2)(2, 0))
