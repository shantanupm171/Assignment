num = int(input("Enter Number: "))
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is Not Prime Number")
            break
    else:
        print(num,"is Prime Number")
else:
    print(num, "is Not Prime Number")