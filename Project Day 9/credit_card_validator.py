ccnumber = list(input("Enter desired credit card number: ").replace(" ", ""))

for i in range(0, len(ccnumber)):
    ccnumber[i] = int(ccnumber[i])

print("Original is: ", ccnumber)
check = ccnumber.pop()
arr = ccnumber[::-1]
print("Result is: ", arr)

index = 0
total = 0
for number in arr:
    if index % 2 == 0 or index == 0:
        double_number = number * 2
        if double_number > 9:
            double_number -= 9
        arr[index] = double_number
    total += number
    index += 1
print("After operation: ", arr)
total += check

if total % 10:
    print("This is a valid card number.")
else:
    print("This is not a valid card number.")