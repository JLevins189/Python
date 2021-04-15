int_str = input("Please give me an integer:")
first_int = int(int_str)
int_str = input("Please give me a second integer:")
second_int = int(int_str)
tens_count = 0
loop_count = 0
while first_int > 10 and second_int < 20:
    if first_int == 10 or second_int == 10:
        tens_count += 1
        first_int -= 5
        second_int += 5
        loop_count += 1
        print(tens_count) # Line 1
        print(loop_count) # Line 2
        print(first_int) # Line 3
        print(second_int) # Line 4