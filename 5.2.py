largest = 0
smallest= 0
while True:
    num = input("Enter a number:")
    if num=="done":
        break
    try:
        n=int(num)
    except:
        print("Invalid input")
        continue
    if n>largest:
        largest=n
    else:
        smallest=n
print("Maximum is",largest)
print("Minimum is",smallest)
