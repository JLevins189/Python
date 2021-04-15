def addfrac(tuple3, tuple4):
    gcd = tuple3[1] * tuple4[1]

    x = tuple3[0] * tuple4[1]
    y = tuple4[0] * tuple3[1]

    new_tuple3 = (x, gcd)
    new_tuple4 = (y, gcd)

    result_tuple = (new_tuple3[0] + new_tuple4[0], gcd)
    return result_tuple


c = int(input("Enter a nominator for fraction 1\n"))
d = int(input("Enter a denominator for fraction 1\n"))
a = int(input("Enter a nominator for fraction 2\n"))
b = int(input("Enter a denominator for fraction 2\n"))

tuple1 = (c, d)
tuple2 = (a, b)

answer = addfrac(tuple1, tuple2)
print(answer)
answerdecimal = answer[0] / answer[1]
print("Answer as decimal is", answerdecimal)
