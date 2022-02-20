from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a list of Question objects from list of question dictionaries.
question_bank = []
for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))

# Create a QuizBrain object using the list of Question objects.
quiz = QuizBrain(question_bank)

# Play quiz game while there are questions left.
while quiz.still_has_questions():
    quiz.next_question()

# Display final score.
print(f"\nYou've completed the quiz")
print(f"You final score was: {quiz.score}/{quiz.question_number}")
