numbers = [1,2,3,12,15,11]
highest = 0
second_highest = 0
for num in numbers:
    if num > highest:
        second_highest = highest
        highest = num

    elif highest > num > second_highest:
        second_highest = num

print("Highest Number is: ", highest)
print("Second Highest Number is: ",second_highest)