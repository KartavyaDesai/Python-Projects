import random
robot = ["Rock", "Scissors", "Paper"]
print("Welcome to the game! It will be best of three...")
u_score = 0
r_score = 0
for _ in range(3):
    robo = random.choice(robot)
    user = input("Choose :")
    print(f"Robot chose: {robo}")
    if(robo==user):
        pass
    elif(robo=="Rock"):
        if user=="Paper":
            u_score=u_score+1
        else:
            r_score=r_score+1
    elif(robo=="Paper"):
        if user=="Scissors":
            u_score=u_score+1
        else:
            r_score=r_score+1
    elif(robo=="Scissors"):
        if user=="Rock":
            u_score=u_score+1
        else:
            r_score=r_score+1
if(u_score > r_score):
    print("You won!")
elif(u_score == r_score):
    print("It's a Tie!")
else:
    print("You lose!")