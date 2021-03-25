hours=input("enter hours")
rate= input("enter rate")
try:
    h=float(hours)
    r=float(rate)
except:
    print("TraceBack error")
    exit()
p=computepay(h,r)
print("Pay",p)
def computepay(hr,rt):
    if hr<=40:
        pay=hr*rt
        return pay
    else:
        pay= ((hr-40)*1.5+40)*rt
        return pay
