def quiz_game():

    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            "answer": "C"
        },
        {
            "question": "What is 5 + 7?",
            "options": ["A. 10", "B. 12", "C. 14", "D. 15"],
            "answer": "B"
        },
        {
            "question": "Who developed Python?",
            "options": ["A. Dennis Ritchie", "B. Guido van Rossum", "C. James Gosling", "D. Bjarne Stroustrup"],
            "answer": "B"
        }
    ]


    score = 0


    for i, q in enumerate(questions, start=1):
        print(f"Question {i}: {q['question']}")
        for option in q['options']:
            print(option)
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")


    print(f"Quiz Over! Your final score is: {score}/{len(questions)}")


quiz_game()


# if __name__ == "_main_":
#     quiz_game()