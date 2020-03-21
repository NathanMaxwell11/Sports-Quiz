# Nathaniel Maxwell
# Integration Project
# Sports Quiz

#Work on Quiz name
#Not Much added this time more of polishing and adding loops and files
points_1 = 0
points_2 = 0
points_3 = 0
points_4 = 0
restarts = 0
w = 0
x = 0
y = 0
z = 0
while x < 1:
    print("1:Start Quiz")
    print("2:Cerdits")
    print("3:Leaderboards")
    print("4:Exit")
    main_menu = int(input("What would you like to do? "))
    if main_menu == 1:
        name = input("Welcome! What is your name? ")
        print(("I hope you enjoy the quiz "), name, ("!"), sep = "")
        print("Here we go")
        x = 2
    elif main_menu == 2:
        while y < 1:
            print("Question by Nathan Maxwell")
            print("Made by Nathan Maxwell")
            print("Are you done?")
            in_credit = int(input("1: yes or 2: no "))
            if in_credit == 1:
                y = 2
                x = 0
            else:
                y = 0
                x = 2
    elif main_menu == 3:
        def main():
            leaderboard_list = open('leaderboard.txt')
            lb = leaderboard_list.read()
            print(lb)
        main()
    elif main_menu == 4:
        print("I hope you enjoyed the quiz!")
        x = 2

# Every question right get 1 pts
# Every question wrong -1 pts and reset
# Checkpoint every 5 questions
# Gets harder as goes on
# POGIL to find what to use and exercises
while z < 1:
    print("Question #1")
    print("Who won the Super Bowl in the 2019-2020 NFL season?")
    print("1:New England Patriots")
    print("2:Kansas City Cheifs")
    print("3:San Fransico 49ers")
    print("4:Green Bay Packers")
    answer_1 = int(input())
    if answer_1 == 1:
        print("You're a year behind")
        points_1 -= 1
    elif answer_1 == 2:
        print("Glad to see you watched the Super Bowl")
        points_1 += 1
    elif answer_1 == 3:
        print("They kinda blew it")
        points_1 -= 1
    elif answer_1 == 4:
        print("No chance at all")
        points_1 -= 1
    print(("You now have: "), points_1, (" point(s)"), sep="")

    print("Question #2")
    print("What NFL team has the most Super Bowl wins?")
    print("1:Pittsburgh Steelers")
    print("2:Dallas Cowboys")
    print("3:San Fransico 49ers")
    print("4:New England Patriots")
    answer_2 = int(input())
    if answer_2 == 1:
        print("You got it")
        points_1 += 1
    elif answer_2 == 2:
        print("Cowboy fans wish")
        points_1 -= 1
    elif answer_2 == 3:
        print("Close but no cigar")
        points_1 -= 1
    elif answer_2 == 4:
        print("Did two right answers trip you up")
        points_1 += 1
    print(("You now have: "), points_1, ( "point(s)"), sep="")

    print("Question #3")
    print("What player in the NBA is known as the Black Mamba")
    print("1:LeBron James")
    print("2:Kobe Bryant")
    print("3:Micheal Jordan")
    print("4:Larry Bird")
    answer_3 = int(input())
    if answer_3 == 1:
        print("Thats King James")
        points_1 -= 1
    elif answer_3 == 2:
        print("What happened is truly sad. Have two points to honor him and Gigi")
        points_1 += 2
    elif answer_3 == 3:
        print("He's the GOAT")
        points_1 -= 1
    elif answer_3 == 4:
        print("Larry Legend")
        points_1 -= 1
    print(("You now have: "), points_1, ( "point(s)"), sep="")

    print("Question #4")
    print("What brand makes NBA jerseys?")
    print("1:Adidas")
    print("2:Under Armour")
    print("3:Nike")
    print("4:Jordan")
    answer_4 = int(input())
    if answer_4 == 1:
        print("Wrong sport")
        points_1 -= 1
    elif answer_4 == 2:
        print("Too small")
        points_1 -= 1
    elif answer_4 == 3:
        print("They are everywhere anymore")
        points_1 += 1
    elif answer_4 == 4:
        print("They just do shoes")
        points_1 -= 1
    print(("You now have: "), points_1, ( "point(s)"), sep="")

    print("Question #5")
    print("What player plays for Argentina in the Mens World Cup?")
    print("1:Cristiano Ronaldo")
    print("2:Neymar Jr")
    print("3:Harry Kane")
    print("4:Lionel Messi")
    answer_5 = int(input())
    if answer_5 == 1:
        print("Plays for Portugal")
        points_1 -= 1
    elif answer_5 == 2:
        print("Plays for Brazil")
        points_1 -= 1
    elif answer_5 == 3:
        print("Plays for England")
        points_1 -= 1
    elif answer_5 == 4:
        print("What a Legend of the sport")
        points_1 += 1
    print(("You now have: "), points_1, ( "point(s)"), sep="")

    print("I'm glad to see you made it past the very easy section.")
    print("Lets see how you're doing.")
    if points_1 >= 4:
        print("You made it past the very easy section!")
        z = 2
    else:
        print("You failed the very easy section and have to redo.")
        z = 0
        points_1 = 0
        restarts =+ 1

print("Your progress is saved. Once you are ready to continue press okay.")
ready = int(input("1:Okay "))
if ready == 1:
    print("Lets go then!")
else: # Would loop
    print("error")

#End of the Quiz
def main():
    name = input("Name: ")
    print("Input the next two numbers you see on the screen.")
    points_lb = input(points)
    restarts_lb = input(restarts)
    in_file = open('leaderboard.txt', "a")
    in_file.write("\nName: " + name)
    in_file.write("\nPoints: " + points_lb)
    in_file.write("\nRestarts: " + restarts_lb)
    in_file.close()
main()

print("Would you like to see the leaderboard?")
print("1:yes")
print("2:no")
look_leaderboard = int(input())
if look_leaderboard == 1:
    while w < 1:
        def main():
            leaderboard_list = open('leaderboard.txt')
            lb = leaderboard_list.read()
            print(lb)
        main()
        print("Press 1 to exit")
        leave = int(input())
        if leave == 1:
            print("I hope you enjoyed the quiz.")
            print("See you next time!")
            w = 2
        else:
            w = 0
else:
    print("I hope you enjoyed the quiz.")
    print("See you next time!")

