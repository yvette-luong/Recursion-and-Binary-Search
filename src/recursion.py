# Problem: Print a list of numbers

"""
print_list_of_numbers(lst):
    print the first number
    print_list_of_numbers(the remaining numbers in the list)


"""

def print_list_of_numbers(lst):
    # base case
    if lst == []:
        return
    print(lst[0], lst)
    print_list_of_numbers(lst[1:])  # recursive call

print_list_of_numbers([0,1,2,3,4,5])


def print_number_range(x, y):
    # base case 
    if x > y :
        return
    print("inbound:", x)
    print_number_range(x+1, y)
    print("outbound:", x)

print_number_range(2,6)
