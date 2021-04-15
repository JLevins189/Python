def tuple_sort(tuple1, tuple2, tuple3):
    new_list = []

    if tuple1[1] > tuple2[1]:
        if tuple1[1] > tuple3[1]:  # Tuple1 >Tuple 2+3
            new_list.append(tuple1)
            if tuple2[1] > tuple3[1]:
                new_list.append(tuple2)
                new_list.append(tuple3)
            else:
                new_list.append(tuple3)
                new_list.append(tuple2)
    elif tuple2[1] > tuple3[1]:  # Tuple 2>Tuple1+3
        new_list.append(tuple2)
        if tuple1[1] > tuple3[1]:
            new_list.append(tuple1)
            new_list.append(tuple3)
        else:
            new_list.append(tuple3)
            new_list.append(tuple1)
    elif tuple3[1] > tuple1[1]:  # Tuple 3>Tuple1+2
        new_list.append(tuple3)
        if tuple1[1] > tuple2[1]:
            new_list.append(tuple1)
            new_list.append(tuple2)
        else:
            new_list.append(tuple2)
            new_list.append(tuple1)

    return new_list


t1a = 'item1'
t1b = float(input("Enter a float for item1\n"))
t2a = 'item2'
t2b = float(input("Enter a float for item2\n"))
t3a = 'item3'
t3b = float(input("Enter a float for item3\n"))

tuple1 = (t1a, t1b)
tuple2 = (t2a, t2b)
tuple3 = (t3a, t3b)
answer = tuple_sort(tuple1, tuple2, tuple3)
print(answer)
