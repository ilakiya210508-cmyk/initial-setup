p=int(input("enter principle:"))
r=float(input("enter rate:"))
t=int(input("enter time:"))
a=p*(1+r/100)**t
CI=a-p
print("compound intrest:",CI)

output

enter principle:1234
enter rate:7.4
enter time:7
compound intrest: 799.9727455254372
