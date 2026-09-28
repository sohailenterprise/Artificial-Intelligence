
correct_answers = ["A", "C", "B", "D", "A"]
user_answers = []

def grade_quiz(user_answers, correct_answers):
    score = 0

    for i in range(len(user_answers)):
        if user_answers[i].upper() == correct_answers[i]:
            score += 1

    attempted = len(user_answers)

    if attempted > 0:
        percentage = (score / attempted) * 100
    else:
        percentage = 0

    return {
        "score": score,
        "attempted": attempted,
        "percentage": percentage
    }

i = 0

while i < len(correct_answers):
    answer = input("Question " + str(i + 1) + " answer (or 'quit' to stop): ")

    if answer.lower() == "quit":
        break

    user_answers.append(answer)
    i += 1


result = grade_quiz(user_answers, correct_answers)

print("score ->", result["score"])
print("attempted ->", result["attempted"])
print("percentage ->", result["percentage"])



