from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# using a for loop to cycle through all the data 
for item in question_data['results']:
     # appending each question to the question bank
     question_bank.append(Question(item['question'],item['correct_answer'],item['category']))

# creating an instance of quiz_brain
quiz = QuizBrain(question_bank)
# using while loop to cycle through all the questions if there are still questions left
while quiz.still_has_question():
     quiz.next_question()   