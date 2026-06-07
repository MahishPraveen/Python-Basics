#Anime Trivia

choice = input("Do you want to play? (yes/no): ")
if choice.lower()=="yes":
    points = 0
    print("Lets Begin!")

    q1 = input("What demon is sealed inside of Naruto?")
    if q1.lower()= "nine tailed fox":
        print("Thats Correct! Good Job!")
        points+=1
    else:
        print("Thats wrong, sorry!")
    
    q2 = input("What Devil Fruit gave Luffy his powers in One Piece?")
    if q2.lower()= "gomu gomu no mi":
        print("Correct! Your Rocking!")
        points+=1
    else:
        print("Thats wrong, sorry!")
    
    q3 = input("What weapons do the Shinigami use in Bleach?")
    if q3.lower()= "zanpakuto":
        print("Thats Correct again, Hatrick!")
        points+=1
    else:
        print("Thats wrong, sorry!")
    
    q4 = input("What’s the name of Killua’s younger, wish-granting sister in Hunter x Hunter?")
    if q4.lower()= "alluka zoldyck":
        print("Correct! Your smooth!")
        points+=1
    else:
        print("Thats wrong, sorry!")

    q5 = input("Which color is NOT used in any of Gojo’s attacks in Jujutsu Kaisen")
    if q5.lower()= "Orange":
        print(Correct! Dayum Godlike!")
        points+=1
    else:
        print("Thats wrong, sorry!")

    print("Quiz Over!")
    print("Your Score=",points,"/5")
else:
    Print("Maybe next time")

    
    
