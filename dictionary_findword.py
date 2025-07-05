dictionary={}
while True:
    print("1.Add word")
    print("2.Find meaning")
    print("3.Update meaning")
    print("4.want entire dictionary")
    print("5.Exit")

    user_1=input("Choose an option: ")

    if user_1=="1":
        choose_=input("Come on add a word you fucker: ").title()
        choose_1=input("Come on fucker enter its meaning: ").title()
        dictionary[choose_]=choose_1
        print("word added and meaning added bey")
    elif user_1=="2":
        find_meaning=input("enter word: ")
        if find_meaning in dictionary:
            print(dictionary[find_meaning])
        elif find_meaning not in dictionary:
            print("No word found")
    elif user_1=="3":
        update_word_and_meaning=input("Enter word: ")
        if update_word_and_meaning not in dictionary:
            update_meaning=input("Enter meaning: ")
            dictionary[update_word_and_meaning]=update_meaning
            print("word updated")
        elif update_word_and_meaning in dictionary:
            print("word already existing ra erri puka")
    elif user_1=="4":
        print(dictionary)
    elif user_1=="5":
        print("Dengey")
        break



