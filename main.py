from my_assistant import *
print(starting)
print(option)
with open("2500 English Words.txt", "r", encoding="utf-8") as the_folder:
    all_words = the_folder.read().splitlines()
score = 0
for n in range(10):
    word = all_words[n].split(maxsplit=1)
    word_en = word[0]
    word_ar = word[1]
    answer = ""
    while answer != word_ar:
        answer = input(f"what is the meaning of ({word_en}) in arabic?: ")
        if answer == word_ar:
            score += 1
            text(score)
            correct_answer(all_words[n])
            print("-"*50)
        elif answer == "r":
            again()
            exit()
        elif answer == "n":
            print(f"the Correct answer is : {word_ar}")
            print("-" * 50)
            break
        elif answer == "q":
            scores(score)
            print("FINISH")
            exit()
        else:
            print("wrong, please try again!")
scores(score)
# This Is My Learn English App
