# Write a list comphrension to print a multiplication table of user entered number

user_no = int(input("Enter the number: "))

# table = []

# for i in range(1,11):
#     table_no = user_no*i
#     table.append(table_no)
#     i +=1

# Shorter way using list comphrension is
table = [user_no*i for i in range(1,11)]
print(table)