hrs = input("Enter Hours:")
h = float(hrs)
rate=input("enter rate")
r=float(rate)
if h<=40:
    print(h*r)
else:
    pay=((h-40)*r*1.5)+(40*r)
    print(pay)
