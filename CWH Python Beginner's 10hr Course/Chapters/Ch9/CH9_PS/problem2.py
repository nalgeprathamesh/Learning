# The game() function lets user play a game and returns the score as an integer. You need to
# read a file high_score.txt which is either blank or contains the previous high score
# You need to write a program to update the high score whenever the game function breaks the high score

score = int(input("Enter the high score: "))

with open("CH9_PS\high_score.txt" , "r") as f:
    content = f.readline()
    if content == "":
        high_score=0
    else:
        high_score=int(content)

if score>high_score:
    with open("CH9_PS\\high_score.txt", "w") as f:
        f.write(str(score)) #We have converted to str bcz write only accepts str
        print("New high score saved")
else:
    print("No new high score")       

# Note that game() function is not defined here bcz its just a practice problem
# Harry sir has used random fn to generate high score in this case instead of input