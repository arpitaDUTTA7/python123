import random
i=0
count1=0
count2=0
while(i<5):
    user_input = (input("Enter a choice : rock, paper, scissors...."))
    possible_action = ["rock", "paper", "scissors"]
    computer_action = random.choice (possible_action)
    print("Your choice is",user_input)
    print("Computer's choice is",computer_action)
    

    if user_input==computer_action:
        print("It's a draw.")
        
    elif user_input=="rock":
        if computer_action == "paper":
           print("You lost.Computer won.")
           count2+=1
        elif computer_action == "scissors":
           print("You won.Computer lost.")
           count1+=1

    elif user_input=="paper":
        if computer_action == "scissors":
           print("You lost.Computer won.")
           count2+=1
        elif computer_action == "rock":
           print("You won.Computer lost")
           count1+=1

    elif user_input=="scissors":
        if computer_action == "paper":
           print("You won.Computer lost.")
           count1+=1
        elif computer_action=="rock":
           print("You lost.Computer won.")
           count2+=1
    i+=1  

if count1 > count2:
     print("You are the ultimate winner.Congratulations!")
elif count1 < count2:
     print("Computer is the ultimate winner.Better luck next time!")
  

