# for loop -- definite number of iterations ( Range , Lists , Tuple )

# while loop -- indefinite number of iterations

for i in range(0, 10, 3):  # start , stop , step
    print(f"Iteration {i}")
    print(f"nimbus is a cloud")

colors = ["yellow", "green", "blue"]
for color in colors:
    print(color)

fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)

# while loop

count = 0
while count < 5:
    print(f"Count is {count}")
    #breakpoint()
    count += 1



for i in range(1, 6):
    if i == 3:
        break  # Stop loop when i equals 3
    print(i)


deployment = ["build", "test", "deploy", "monitor"]
for stage in deployment: 
    if stage == "test":
        print("skipping tests...")
        continue 
    print(f"Completed stage: {stage}")
print("Deployment process finished.")