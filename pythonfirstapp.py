import math
import random
import datetime
import time

customer = []
marks = []
height_limit = 0.5
levels = []

"""
********************************************************************************************************************
About: : program take the input as the user name, and time. afetr that according to time,
it display good morning, good afternoon or good evening.
********************************************************************************************************************
"""


def user():
    user = raw_input("plesae enter Your name ")
    timming1 = raw_input("please enter time (In 24 hrs clock)? and HH:MM:SS format ")
    timming = datetime.datetime.strptime(timming1, "%H:%M:%S")
    # timming = raw_input("please enter time (In 24 hrs clock)? ")
    # time.timming =(timming,"%H:%M:%S")

    case1 = datetime.datetime.strptime("12:00:00", "%H:%M:%S")
    case2 = datetime.datetime.strptime("18:00:00", "%H:%M:%S")

    if timming < case1:
        print 'Good Morning ' + str(user)
    elif timming < case2:
        print 'Good Afternoon ' + str(user)
    elif timming >= case2:
        print 'Good Evening ' + str(user)
    else:
        print 'entertime into HH:MM:SS'


"""
********************************************************************************************************************
About: program is sue to print the name.
********************************************************************************************************************
"""


def name():
    print """
        * * *  ******* ******   ******  *****  *     *  *******  *******  *****
        *         *    *        *       *   *  * *   *     *        *     *   *
        * * *     *    ******   ******  *****  *  *  *     *        *     ***** 
            *     *    *        *       *   *  *   * *     *        *     *   *
        * * *     *    ******   *       *   *  *    **  *******     *     *   *
        """


"""
********************************************************************************************************************
About:for this program, user have to provids the radius as a input, after that it will display the perameter and area of circle.

********************************************************************************************************************
"""


def main(rad):
    perimeter = 2 * 3.14 * rad
    area = 3.14 * rad * rad
    return (perimeter, area,)


def circle():
    rad = float(raw_input("input radius "))
    print main(rad)


"""
********************************************************************************************************************
About:user have to put the average speed and then this will display the time of reaching.
********************************************************************************************************************
"""


def dis(average_speed):
    if average_speed < 18:
        print 'please enter greater than 18'
    else:
        dis = 300
        starting_time = 6
        time = dis / average_speed

        reach_time = starting_time + time
        return reach_time


def time1():
    average_speed = float(raw_input("average speed? "))
    print dis(average_speed)


"""
********************************************************************************************************************
About:  program take the marks from of the user, after that it calcualte the avearge marks. afetr that according to the marks it shows the result,
fail, pass, merit and distinction.
********************************************************************************************************************
"""


def grade2():
    name = raw_input("What's your name? ")
    mark = int(raw_input("Enter your grade (0-100)? "))

    customer.append(name)
    marks.append(mark)

    if mark < 40:
        levels.append("Fail")
    elif mark <= 60:
        levels.append("Pass")
    elif mark <= 80:
        levels.append("Merit")
    elif mark <= 100:
        levels.append("Distinction")

    cmd = raw_input("Press 'y' to continue. Anything else to quit: ")
    if cmd != 'y':
        sum_grade = 0
        for i in range(len(customer)):
            sum_grade = sum_grade + marks[i]
            print str(customer[i]) + "  " + str(marks[i]) + "  " + str(levels[i])

        print "Avg grade is " + str(sum_grade / len(customer))
    # break


def grade1():
    while True:
        grade2()

    """
********************************************************************************************************************
About:  this program is generate the ramdon numbers for the draws.
********************************************************************************************************************
"""


def newgame(draws):
    for i in range(draws):
        print 'Draw ' + str(i + 1)
        row = []
        for j in range(6):
            no = random.randint(1, 60)  # Generate Random Number
            row.append(no)

        for item in row:
            print item


def game1():
    draws = int(raw_input("Enter draws: "))
    newgame(draws)


"""
********************************************************************************************************************
About:  this program firstly intialize an array and after that sum the values present into the array.
********************************************************************************************************************
"""


def arr(newarray):
    sum = 0
    for item in newarray:
        sum = sum + item
    return sum


def values():
    newarray = [1, 4, 5, 7, 3, 8]
    print arr(newarray)
    """
********************************************************************************************************************
About:  shows the number of bounce, for that user have to input the height in cm.
********************************************************************************************************************
"""


def bounceheight():
    height = float(raw_input("provide height (in cm): "))
    actual_height = height
    bounces = 0

    while actual_height > height_limit:
        bounces = bounces + 1
        actual_height = 0.75 * actual_height
        print bounces


"""
****************************************************************************************************
About:  this is use to generate the random questions, with the use of random numbers and random operations.
*****************************************************************************************************
"""


def random_maths_questions():
    values = int(input("number of questions to generate"))

    stop = False
    ques = 0
    cques = 0

    while stop == False:
        choice = random.choice("+-x/")
        if ques < values | ques >= 0:
            number1 = random.randrange(1, 10)
            number2 = random.randrange(1, 10)
            print((number1), (choice), (number2))
            ans = int(input("provide answer"))
            ques = ques + 1

            if choice == ("+"):
                exactans = number1 + number2
                if ans == exactans:
                    print("correct answer try next")
                    cques = cques + 1
                else:
                    print("Wrong answer,the correct answer", exactans, "!")

            if choice == ("x"):
                exactans = number1 * number2
                if ans == exactans:
                    print("correct answer try next")
                    cques = cques + 1
                else:
                    print("Wrong answer, the answer ", exactans, "!")

            elif choice == ("-"):
                exactans = number1 - number2

                if ans == exactans:
                    print("correct answer try next")
                    cques = cques + 1
            elif choice == ("/"):
                exactans = number1 / number2

                if ans == exactans:
                    print("correct answer try next")
                    cques = cques + 1
                else:
                    print("Wrong answer, the answer", exactans, "!")
        else:
            stop = True
    else:
        print("Quiz completed")
        print("You scored " + str(cques))


ans = True
while ans:
    print ("""
    1.1 Hello C# 
    1.2 Your Name Characters
    1.3 The Area and the perimeter of a Circle
    1.4 Time of Journey
    1.5 The Student Examination Results Analysis
    1.6 The National Lottery Number Generator
    1.7 The Sum of the Elements of an Array
    1.8 Bouncing Ball Game
    1.9 Maths practice questions 
    1.10 Exit 
    """)
    ans = raw_input("Select one option: ")

    if ans == "1.1":
        user()
    elif ans == "1.2":
        name()
    elif ans == "1.3":
        circle()
    elif ans == "1.4":
        time1()
    elif ans == "1.5":
        grade1()

    elif ans == "1.6":
        game1()
    elif ans == "1.7":
        values()
    elif ans == "1.8":
        bounceheight()
    elif ans == "1.9":
        random_maths_questions()
    elif ans == "1.10":
        print 'You are exited from program'
        break
