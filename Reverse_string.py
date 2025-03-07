# Create a Python function that takes a
# string as input and returns the reverse of
# that string. For example, if the input is
# "hello," the function should return
# "olleh."
def reverse_string(x):
    return x[::-1]

x=input("Enter String:-")
print(reverse_string(x))