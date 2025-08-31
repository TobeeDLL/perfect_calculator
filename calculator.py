print("Welcome to my calculator!\n")


# ========================
# User Input            ||
# ========================

astr = input("Enter first number: ")
if not astr.isdigit():
    print(f"Invalid Value! '{astr}' must be a number")
    exit()

oper = input("What operation to preform (+ - x ^): ")
if not (len(oper) == 1 and oper in ["+", "-", "x", "^"]):
    print(f"Invalid Operation! '{oper}' has to be '+' '-' 'x' or '^'")
    exit()

bstr = input("Enter second number: ")
if not bstr.isdigit():
    print(f"Invalid Value! '{bstr}' must be a number")
    exit()

expectationstr = input("What do you think the result is: ")
if not expectationstr.isdigit():
    print(f"Invalid Value! '{expectationstr}' must be a number")
    exit()


# ========================
# Variables             ||
# ========================

a = int(astr)
b = int(bstr)
result = 0
expectation = int(expectationstr)


# ========================
# Operations            ||
# ========================

if oper == '+':
    tmp = a
    for i in range(b):
        tmp = tmp + 1
    result = tmp

elif oper == '-':
    tmp = a
    for i in range(b):
        tmp = tmp - 1
    result = tmp

elif oper == 'x':
    for j in range(b):
        for i in range(a):
            result = result + 1

elif oper == '^':
    for l in range(b-1):
        for j in range(a):
            for i in range(a):
                result = result + 1


# ========================
# Results               ||
# ========================

guessed = False

if result == expectation:
    guessed = True

print(f"{guessed}! {a} {oper} {b} = {result}")
