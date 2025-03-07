#season = input("What is your favoutite season? \n: ")
#seasons_list = ["winter", "summer", "autumn", "spring", "fall"]
#
#if season.lower().strip() in seasons_list:
#    print("real")
#else:
#    print("Drugs!!!! That is not a season!!!!")

# fisrt bible book
bible_books = ["genesis", "exodus", "numbers", "leviticus", "a", "b", "c", "d"]
first_book = input("""What is the first book of the Bible? 
                   a) genesis
                   b) exodus
                   c) numbers
                   d) leviticus
                   
                   :""")

if first_book.lower().strip() in bible_books:
    if first_book.lower().strip() == "genesis" or "a":
        print("Ding ding ding!!!!! Correct, you just won a million dollars!!!!")
    else:
        print("Nope!! you're wrong!! Skill issue GET OUT!!!!")
else:
    print("Thats not even an option????")