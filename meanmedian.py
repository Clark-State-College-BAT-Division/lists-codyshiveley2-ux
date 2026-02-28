#prompt the user to enter 5 numbers. Store them in a list.
#Display the list as entered, small to large, and large to small
#Calculate and display the mean and median
#This is a guided practice. You can follow the video or your instructor will go
#over this in class
# video url: https://youtu.be/VGrRdUunjXg


numbers = []

for i in range(5):
    num = float(input("Enter a number: "))
    numbers.append(num)


print("\nNumbers as entered:")
print(numbers)


ascending = sorted(numbers)
print("Small to large:")
print(ascending)


descending = sorted(numbers, reverse=True)
print("Large to small:")
print(descending)


mean = sum(numbers) / len(numbers)

1
ascending_sorted = sorted(numbers)
mid = len(ascending_sorted) // 2

if len(ascending_sorted) % 2 == 1:
    median = ascending_sorted[mid]
else:
    median = (ascending_sorted[mid - 1] + ascending_sorted[mid]) / 2

print(f"\nMean: {mean}")
print(f"Median: {median}")

