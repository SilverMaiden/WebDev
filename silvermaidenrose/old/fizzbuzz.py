def fizzbuzz(n):
    x = 0
    while x != n:
        x += 1
        if (x % 3 == 0 and x % 5 != 0):
            print "fizz"
        elif (x % 3 != 0 and x % 5 == 0):
            print "buzz"
        elif (x % 3 == 0 and x % 5 == 0):
            print "fizzbuzz"
        else:
            print(x)


print fizzbuzz(3)
