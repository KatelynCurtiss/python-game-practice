# Katelyn Curtiss
# 15 Novemeber 2024
# Python Game Practice

def ask_questions(question, answer):
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        return True
    