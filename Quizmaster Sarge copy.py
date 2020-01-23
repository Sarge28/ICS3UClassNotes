import time
import random
print(" $$$$$$\                                                           $$$$$$\            $$\ ")  # used for cool personalized experience
time.sleep(1)
print("$$  __$$\                                                         $$  __$$\           \__|")
time.sleep(1)
print("$$ /  \__| $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$$\       $$ /  $$ |$$\   $$\ $$\ $$$$$$$$\ ")
time.sleep(1)
print("\$$$$$$\   \____$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  _____|      $$ |  $$ |$$ |  $$ |$$ |\____$$  | ")
time.sleep(1)
print(" \____$$\  $$$$$$$ |$$ |  \__|$$ /  $$ |$$$$$$$$ |\$$$$$$\        $$ |  $$ |$$ |  $$ |$$ |  $$$$ _/")
time.sleep(1)
print("$$\   $$ |$$  __$$ |$$ |      $$ |  $$ |$$   ____| \____$$\       $$ $$\$$ |$$ |  $$ |$$ | $$  _/")
time.sleep(1)
print("\$$$$$$  |\$$$$$$$ |$$ |      \$$$$$$$ |\$$$$$$$\ $$$$$$$  |      \$$$$$$ / \$$$$$$  |$$ |$$$$$$$$\ ")
time.sleep(1)
print(" \______/  \_______|\__|       \____$$ | \_______|\_______/        \___$$$\  \______/ \__|\________|")
time.sleep(1)
print("                              $$\   $$ |                               \___|")
print("                              \$$$$$$  |")
time.sleep(1)
print("                               \______/")
time.sleep(5)
print("Now here are some rules, answer the questions and have fun.")
time.sleep(2)
running = True
while running == True:  # while loop for  multiple runs through the game
    quiz_choose = input("Do you to play the minecraft or baseball quiz?")  # input for certain quiz
    quiz_choose.lower()  # makes variable lowercase to make if statement true/false
    file = 0
    answerfile = 0
    highscorefile = 0
    score = 0
    question = 0
    answers = 0
    if quiz_choose == str("minecraft"):
        try:
            file = open("QuizMinecraftQuestions.txt", "r")  # opens all files needed for the chosen quiz(questions/answers/highscores)
            answerfile = open("QuizMinecraftAnswers.txt", "r")
            highscorefile = open("QuizMinecraftHighscores.txt", "a")
        except IOError:
            print("Come see Sarge for assistance")  # try except is just in case the files aren't there
    elif quiz_choose == str("baseball"):
        try:
            file = open("QuizBaseballQuestions.txt", "r")  # opens all files needed for the chosen quiz(questions/answers/highscores)
            answerfile = open("QuizBaseballAnswers.txt", "r")
            highscorefile = open("QuizBaseballHighscores.txt", "a")
        except IOError:
            print("Come see Sarge for assistance")  # try except is just in case the files aren't there
    questions = file.readlines()
    answers = answerfile.readlines()
    data = [0,1,2,3,4,5,6,7,8,9]  # list for randomizing the order of questions/answers
    random.shuffle(data)  # .shuffle is used to change order of the list
    for i in data:
        user_answer = input(questions[i])  # the question is printed at the i  value which is random from the .shuffle function then if the input is = to the answer from the  other list then the the score is increased by 1
        user_answer = user_answer.lower()
        if user_answer == answers[i].strip():  # the .strip function clears the contents of the variable so it can be used again
            print("Correct")
            score = score + 1
        elif user_answer != answers[i].strip():
            print("Incorrect")
    print("Thank you for playing you scored", score,"/10")  # prints score
    time.sleep(2)
    name = input("Write three letters to save your score!")  # allows people to see there previous scores
    name = name.upper()
    name += str(score) + ("/10")
    highscorefile.write(name+"\n")  # saves scores to highscore files
    time.sleep(2)
    if quiz_choose == str("minecraft"):
        highscorefile = open("QuizMinecraftHighscores.txt", "r")
    elif quiz_choose == str("baseball"):
        highscorefile = open("QuizBaseballHighscores.txt", "r")
    print("These are the scores from previous games\n", highscorefile.read())  # opens highscore files to read the contents(all the scores)
    time.sleep(5)
    continue_running = input("Do you want to try again or a different quiz? Yes or No")
    continue_running.lower()
    if continue_running == ("yes"):  # just runs again or not
        running = True
    elif continue_running == ("no"):
        running = False