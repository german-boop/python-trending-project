questions = {
    "Capital of France?": "Paris",
    "5 + 7 = ?": "12",
    "Python creator?": "Guido"
}

score = 0
for q, a in questions.items():
    answer = input(q + " ")
    if answer.strip().lower() == a.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
print(f"Your score: {score}/{len(questions)}")
