# def sum(num):
#     n=0
#     for i in range(1,num+1):
#         n += i
#     return n
# num = 5
# print(sum(num))

# def sum_of_natural_numbers(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total

# # Example usage:
# n = 5
# print("Sum of first", n, "natural numbers is:", sum_of_natural_numbers(n))


def sum_of_natural_numbers(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)

# Example usage:
n = 5
print("Sum of first", n, "natural numbers is:", sum_of_natural_numbers(n))


def sum(n):
    if(n<=0):
        return 0
    else:
        return n + sum(n-1)

n=5
print(sum(n))
