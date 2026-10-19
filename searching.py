arr=[10,20,30,40,50,60,70]
for i in range(len(arr)):
    if arr[i]==60:
        print("found at index",i)
        break
else:
    print("not")
