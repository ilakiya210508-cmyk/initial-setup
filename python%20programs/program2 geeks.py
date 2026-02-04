#using if else

a=int(input("enter:"))
b=int(input("enter:"))
if a>b:
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")
    
#another method using ternary operator  
  
print(a if a>b else b)

#using max function

print(max(a,b))

#using sort

n=[a,b]
n.sort()
print(n[-1])
