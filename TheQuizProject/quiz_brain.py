class QuizBrain:
     def __init__(self,list):
          # initializing the constructors
          self.question_number = 0
          self.question_list = list
          self.score = 0
          
     def next_question(self):
          print(f"The category for this question is: {self.question_list[0].category}")
          # asking the user for input
          user_answer = input(f"Q.{self.question_number+1}: {self.question_list[0].question}?: ")
          # incrementing the question number
          self.question_number +=1
          # calling the check_answer() method to check answer
          self.check_answer(user_answer) 
          
     def still_has_question(self):
          # returns true if there are still questions in question bank
          return len(self.question_list) > 0
     
     def check_answer(self,user_answer):
          # if the input answer match the answer
          if user_answer.lower() == self.question_list[0].answer.lower():
               # increment the score
               self.score +=1
               print("Your answer was correct")
          else:
               print("Your answer was incorrect")
          # print the correct answer
          print(f"The correct answer is {self.question_list[0].answer}\nYour score is {self.score}\n")   
          # remove this question from the question bank
          self.question_list.remove(self.question_list[0])