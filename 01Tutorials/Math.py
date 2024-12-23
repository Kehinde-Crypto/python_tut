print("add")
my_num = 5 + 5
print(my_num)

print("integer division")
my_number = 7//2 # it does not give the remainder 7 % 2
print(my_number)

# functions is  a self contained reuseable chuck of logic
def print_integer():
 print("hi")
 print_integer() # invocation of print integer
def my_word(word):
 print(word)
my_word("hi") # invocation

def add_six(my_number):
 print(my_number + 6)
 add_six(my_number + 16)
 

