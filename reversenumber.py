
""" Reverse the number given

    Accept the number(int) input
    Reverse the given number
"""

# # given list of number method
# normal_number = [5, 4, 3, 2, 1]
# normal_number.reverse()
# print(normal_number)

# standard input method
while True:
    number_input = int(input())
    splitted_list = list(str(number_input))
    splitted_list.reverse()
    combined_string = ''.join(splitted_list)
    combined_number = int(combined_string)
    print(combined_number)