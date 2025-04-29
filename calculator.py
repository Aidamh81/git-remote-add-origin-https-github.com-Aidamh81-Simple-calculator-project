
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b

print("عملیات: + - * /")
op = input("عملیات مورد نظر را وارد کن: ")
x = float(input("عدد اول: "))
y = float(input("عدد دوم: "))

if op == "+":
    print("نتیجه:", add(x, y))
elif op == "-":
    print("نتیجه:", subtract(x, y))
elif op == "*":
    print("نتیجه:", multiply(x, y))
elif op == "/":
    print("نتیجه:", divide(x, y))
else:
    print("عملیات نامعتبر")
