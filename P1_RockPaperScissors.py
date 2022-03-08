import random


userInput=input("Enter your option ( rock / paper / scissors )  :   ")   # Taking user input of element which second person will choose who is playing 
userInput=userInput.lower()# If user will enter element which is containing uppercase letter the it will convert into lower so that it will not show wrror and ferther conditions will check also

Elements=["rock","paper","scissors"]  # Taking all three elements in a list so that computer can take random coice from it 
computer=random.choice(Elements)   # Storing value which computer took randomly 

if computer=="rock" and userInput=="scissors" or computer=="paper" and userInput=="rock" or computer=="scissors" and userInput=="paper":  #  these  are all possible conditions where user loose like if user entered paper and computer choose scissors . IN THIS I HAVE ADDED SENARIOS WERE USER ENTERED ELEMENT WILL START WITH CAPITAL LETTER.
    print("computer : ",computer,"\nuserInput : ",userInput,"\n\n***YOU LOOSE***")  # Printing That who won with both the element which computer choosen and what user gave in user input 

elif computer==userInput:  # Condition is saying that is user and computer will choose same elements then game will be tie
    print("computer : ",computer,"\nuserInput : ",userInput,"\n\n++++ GAME TEI ++++")

elif userInput =="rock" and computer=="scissors" or userInput =="paper" and computer=="rock" or userInput =="scissors" and computer=="paper":  # These are all possible conditions when user can win like if user entered paper and computer choose rock. 
    print("computer : ",computer,"\nuserInput : ",userInput,"\n\n***YOU WIN***")

else:   #  If user will enter any element which is not the part of game then game will stop and it will show element of computer and user as well 
    print("computer : ",computer,"\nuserInput : ",userInput,"\n\nPLEASE ENTER VALID ELEMENT")







