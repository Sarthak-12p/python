print("Welcome to my computer quiz")

playing =  input("Do you want to play? ")

if playing.lower() != "yes" :
    quit()

print("Let's play ")
score = 0 

answer =input("What does CPU stands for ? ")
if answer == "central processing unit" :
    print("Correct!")
    score +=1
else :
    print("Wrong!")

answer =input("What does CPU stands for ? ")
if answer.lower() == "central processing unit" :
    print("Correct!")
    score +=1
else :
    print("Wrong!")

answer =input("What does CPU stands for ? ")
if answer.lower() == "central processing unit" :
    print("Correct!")
    score +=1
else :
    print("Wrong!")

answer =input("What does CPU stands for ? ")
if answer.lower() == "central processing unit" :
    print("Correct!")
    score +=1
else :
    print("Wrong!")

answer =input("What does CPU stands for ? ")
if answer.lower() == "central processing unit" :
    print("Correct!")
    score +=1
else :
    print("Wrong!")


print("You got" + str(score) + "question correct!")
print("You got" + str((score/4) *100) + "%")
    
    


    
