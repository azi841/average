num = int(input("How many numbers?"))
total_sum = 0

for i in range(num):
    numbers = int(input("Enter a number: "))
    total_sum += numbers
    print(total_sum)

avg = total_sum / num

print("Average is: ", int(avg))