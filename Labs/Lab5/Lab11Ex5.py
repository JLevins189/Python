def addfrac(tuple3, tuple4):

    nom = tuple3[0] * tuple4[0]
    denom = tuple3[1] * tuple4[1]

    result_tuple = (nom, denom)
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
