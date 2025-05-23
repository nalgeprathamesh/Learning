for i in range(100):
    if i == 34:
        break  # Exit this loop right now
    print(i)

# This will break the loop when value reaches 34

for i in range(100):
    if i == 70:
        continue  # Skip this iteration
    print(i)

# continue will skip the iteration meaning it will not look at code lines below it instead it
# will continue the loop skipping when i == 70
