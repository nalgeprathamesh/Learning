# Write a program to detect spam in comment
comment = input("Enter your comment ")
# spam = "money", "buy now" , "subscribe" , "click" , "earn money"
spam1 = "money"
spam2 = "buy now"
spam3 = "subscribe"
spam4 = "click"
spam5 = "earn money"

if(spam1 in comment or spam2 in comment or spam3 in comment or spam4 in comment or spam5 in comment):
    print("This comment contains spam")
else:
    print("This comment probably doesn't contain spam")