# Generate a table generator that generates table from 2 to 20 and writes it to different files in a folder for a 13yr old

def tableGenerate(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"

    with open(f"CH9_PS//tables//table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2,21):
    tableGenerate(i)