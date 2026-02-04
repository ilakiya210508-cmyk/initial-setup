n=int(input("enter:"))
dig=0
ori=n
while(ori!=0):
    rem=ori%10
    dig+=rem*rem*rem
    ori=ori//10


if(n==dig):
    print("armstrong number")
else:
    print("not an armstrong number")

output

enter:45
not an armstrong number
