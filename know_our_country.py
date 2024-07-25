from random import shuffle
qus = [
    ("What is name of your country", "india"),
    ("What is the capital of your country", "new delhi"),
    ("What is the national flower ", "lotus"),
    ("what is the name of your national animal", "tiger"),
    ("what is your bird's name", "peocock"),
    ("what is your national flag", "tiranga")
]
shuffle(qus)
right = 0
wrong = 0
for question, right_ans in qus:
    ans = input(question + " ")
    if ans.lower() == right_ans:
        right +=1
    else:
        print("No the right ans is:", right_ans)
        wrong +=1
print("Congratulation !")
print("You gave ", right, "right answers and", wrong, "wrong answers")