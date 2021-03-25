largest = None
smallest = None
i=0
array = []
while True:
    num= input("Enter a number: ")
    if num == "done" :
        break
    try:
        n=int(num)
        #array[i]=n
        #i=i+1
    except:
    #    print("Invalid input")
        continue
print(array)
