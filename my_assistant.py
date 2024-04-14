starting = "=========================\nWelcome To MY Learn English App\n========================="
option = "<---write (n) for the unknowing answer or (q) to quit the program or (r) to test your Solution--->"

def text(score):
    if score == 1:
        print(f"Correct answer, you have memorized {score} word")
    else:
        print(f"Correct answer, you have memorized {score} words")


def correct_answer(current_answer):
    with open("The_new_file.txt", "a", encoding="utf_8") as the_file:
        the_file.write(current_answer + "\n")

    total = ""
    with open("2500 English Words.txt", "r", encoding="utf-8") as file:
        all_text = file.read().splitlines()

    for line in all_text:
        if line != current_answer:
            total += line + "\n"
    with open("2500 English Words.txt", "w", encoding="utf-8") as saved:
        saved.write(total)

def scores(score):
    if score == 10:
        print("Great, you have memorized 10 words, GOOD JOB :)")
    elif score >= 6:
        print(f"Very Good, you have memorized {score} words, GOOD JOB :)")
    elif score >= 2:
        print(f"Good, you have memorized {score} words.Keep going :)")
    elif score == 1:
        print("you need more practice. You have memorized only 1 word, and practice makes you better!")
    else:
        print("You need more practice. You didn't know any word, and practice makes you better!")


def again():
    with open("The_new_file", "r", encoding="utf-8") as the_file:
        f = the_file.read().splitlines()
    score1 = 0
    for w in range(9):
        word2 = f[w].split()
        word2_en = word2[0]
        word2_ar = word2[1]
        answer1 = ""
        while answer1 != word2_ar:
            answer1 = input(f"what is the meaning of ({word2_en}) in arabic?: ")
            if answer1 == word2_ar:
                score1 += 1
                text(score1)
                print("-"*50)
            elif answer1 == "n":
                print(f"the Correct answer is : {word2_ar}")
                print("-" * 50)
                break
            elif answer1 == "q":
                print("FINISH")
                exit()
            else:
                print("wrong, please try again!")
    print(f"You remembered {score1} solutions from your previous solutions")
# This is my assistant in the project