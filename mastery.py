while True:
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    student_id = input("What is your student ID?: ")
    class_one = input("What is your first class? (6 CHARACTERS AND UP) Type STOP to end: ")
    if (class_one == "STOP"):
        print("You have stopped the program.")
        break
    roomnum_one = int(input("What is that classes' room number?: "))
    class_two = input("What is your next class? (6 CHARACTERS AND UP) Type STOP to end: ")
    if (class_two == "STOP"):
        print("You have stopped the program.")
        break
    roomnum_two = int(input("What is that classes' room number?: "))
    class_three = input("What is your next class? (6 CHARACTERS AND UP) Type STOP to end: ")
    if (class_three == "STOP"):
        print("You have stopped the program.")
        break
    roomnum_three = int(input("What is that classes' room number?: "))
    class_four = input("What is your next class? (6 CHARACTERS AND UP) Type STOP to end: ")
    if (class_four == "STOP"):
        print("You have stopped the program.")
        break
    roomnum_four = int(input("What is that classes' room number?: "))
    class_five = input("What is your next class? (6 CHARACTERS AND UP) Type STOP to end: ")
    if (class_five == "STOP"):
        print("You have stopped the program.")
        break
    roomnum_five = int(input("What is that classes' room number?: "))
    class_six = input("What is your next class? (6 CHARACTERS AND UP) Type STOP to end: ")
    if (class_six == "STOP"):
        print("You have stopped the program.")
        break
    roomnum_six = int(input("What is that classes' room number?: "))

        if (len(class_one) <= 5):
        class_one = (class_one + "\t")
    if (len(class_two) <= 5):
        class_two = (class_two + "\t")
    if (len(class_three) <= 5):
        class_three = (class_three + "\t")
    if (len(class_four) <= 5):
        class_four = (class_four + "\t")
    if (len(class_five) <= 5):
        class_five = (class_five + "\t")
    if (len(class_six) <= 5):
        class_six = (class_six + "\t")
    
    print("*************************************************\n*\t\t\t\t\t\t*\n*\t{}, {}\t\t ID:{} \t*\n*\t\t\t\t\t\t*\n*************************************************\n*\t\t\t\t\t\t*\n*\t Class 1: {}\t Room: {}\t*\n*\t Class 2: {}\t Room: {}\t*\n*\t Class 3: {}\t Room: {}\t*\n*\t Class 4: {}\t Room: {}\t*\n*\t Class 5: {}\t Room: {}\t*\n*\t Class 6: {}\t Room: {}\t*\n*\t\t\t\t\t\t*\n*************************************************\n*\t\t\t\t\t\t*\n*************************************************".format(last_name, first_name, student_id, class_one, roomnum_one, class_two, roomnum_two, class_three, roomnum_three, class_four, roomnum_four, class_five, roomnum_five, class_six, roomnum_six))
    break