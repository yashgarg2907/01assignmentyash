# Create your own kbc game :
start_game=input("Do you want to start the game? (yes/no):")
if start_game == "yes":
    score=0
    correct=0
    wrong=0
    skipped=0
    #Qusestion 1
    print("\nQuestion 1 ")
    print("Pyhton kisne banayi ?")
    print("A. james")
    print("B. Guico")
    print("c. Elon")
    print("D. mark")
    answer=input("Enter option(A/B/C/D or skip):")
    if answer == "B":
        score=score+1000
        correct = correct+1
        print("Correct answer")
    elif answer == "skip":
        skipped=skipped+1
        print("Question skipped")
    else :
        wrong=wrong+1
        print("wrong wrong")
    #Qusetion 2
    print("/nQuestion 2")
    print("what is capital of mp?")
    print("A. Indore")   
    print("B. Bhopal")
    print("C. Gwalior")
    print("D. Jawalpur")
    answer=input("Enter option(A/B/C/D or skip):")
    if answer == "B":
        score==score+2000
        correct=correct+1
        print("Correct answer")
    elif answer == "skip":
        skipped=skipped+1
        print("Question skipped")
    else:
        wrong=wrong+1
        print("Question wrong")
    #Question 3
    print("/nQuestion 3")
    print("56 - 16 =?")
    print("A. 45")
    print("B. 56")
    print("c. 50")
    print("D. 40")
    answer=input("Enter option(A/B/C/D or skip):")
    if answer == "D":
        score=score+3000
        correct=correct+1
        print("Correct answer")
    elif answer == "skip":
        skipped=skipped+1
        print("Question skipped")
    else:
        wrong=wrong+1
        print("Question wrong")
    #Question 4
    print("/nQuestion 4")
    print("5 * 4 = ?")
    print("A. 45")
    print("B. 25")
    print("C. 20")
    print("D. 18")
    answer=input("Enter option(A/B/C/D or skip):")
    if answer == "C":
        score=score+4000
        correct=correct+1
        print("Correct answer")
    elif answer == "skip":
        skipped=skipped+1
        print("Question skipped")
    else:
        wrong=wrong+1
        print("Question wrong")
    #Question 5
    print("/nQuestion 5")
    print("who win first team of ipl titel?")
    print("A. Chennai super kings")
    print("B. Mumbai indians")
    print("C. Deccan charger ")
    print("D. pujab kings")
    answer=input("Enter option (A/B/C/D or skip):")
    if answer== "A":
        score=score+5000
        correct=correct+1
        print("Question correct")
    elif answer == "skip":
        skipped=skipped+1
        print("Question skipped")
    else:
        wrong=wrong+1
        print("Question wrong")
    # Final Result
    print(f"Total ssore : {score}")
    print(f"Correct Answers : {correct}")
    print(f"Wrong Answers : {wrong}")
    print(f"Skipped Questions : {skipped}")
else:
    print("Game Cancelled")