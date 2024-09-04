# def calculate_statistics(numbers):
#     total_sum = 0
#     cumulative_sum = []
    
#     for num in numbers:
#         num = float(num)
#         total_sum += num
#         cumulative_sum.append(total_sum)
    
#     return total_sum, cumulative_sum, total_sum / len(numbers), min(numbers), max(numbers)

# user_input = input("Enter a list of numbers separated by spaces: ")
# numbers = user_input.split()
# numbers = [float(num) for num in numbers]

# total_sum, cumulative_sum, average, min_val, max_val = calculate_statistics(numbers)

# print("Sum:", total_sum)
# print("Cumulative Sum:", cumulative_sum)
# print("Average:", average)
# print("Minimum:", min_val)
# print("Maximum:", max_val)

#Question 2 : Question 2:- write a program to take inputs from the user and store them in a list.

#Case 1 : n is defined by user.
#Case 2 : user can enter numbers as per the requirements.

# Case 1: User defines 'n'
# n = int(input("Enter the number of elements you want to add to the list: "))
# numbers_case1 = []

# for i in range(n):
#     number = float(input(f"Enter number {i + 1}: "))
#     numbers_case1.append(number)

# print("List of numbers (Case 1):", numbers_case1)

# # Case 2: User enters numbers until they type "stop"
# numbers_case2 = []

# print("Enter numbers one by one. Type 'stop' to finish:")
# while True:
#     user_input = input()
#     if user_input.lower() == 'stop':
#         break
#     numbers_case2.append(float(user_input))

# print("List of numbers (Case 2):", numbers_case2)

def display(list1)->None:
    total=0
    list2=[]
    for i in list1:
        total=total+i
        list2.append(total)
        
    length=len(list1)
    result = {
        'sum': total,
        'cumulative_sum': list2,
        'average': total / length if length > 0 else 0,
        'min': min(list1),
        'max': max(list1)
    }
    return result


def input_from_user_element():
    n=int(input("Enter the number :"))
    list1=[]
    for i in range(0,n):
        user=int(input("enter the element {i}"))
        list1.append(user)
    val=display(list1)
    print(val)
    
input_from_user_element()
