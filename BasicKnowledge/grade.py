# Calculating Grade Using elif

option = 'Y'
while option == 'Y':
    score = int(input("Input your score: "))

    if score >= 80 and score <= 100:
        print("Your Score\t: ", score, "\nGrade\t: A")
        option = 'N'
    elif score >= 70 and score <= 79:
        print("Your Score\t: ", score, "\nGrade\t: B")
        option = 'N'
    elif score >= 55 and score <= 69:
        print("Your Score\t: ", score, "\nGrade\t: C")
        option = 'N'
    elif score >= 40 and score <= 54:
        print("Your Score\t: ", score, "\nGrade\t: D")
        option = 'N'
    elif score >= 0 and score <= 39:
        print("Your Score\t: ", score, "\nGrade\t: E")
    else:
        print("Please insert the corrent score! [0 - 100]")
    