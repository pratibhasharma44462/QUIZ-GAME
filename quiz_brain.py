class QuizBrain:
    def __init__(self, Q_list):
        self.question_number = 0
        self.question_list = Q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)    
   

    def next_question(self):
        current_question = self.question_list[self.question_number]    
        self.question_number +=1
        choice = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_Answer (choice, current_question.answer)

    def check_Answer(self, user_answer, correct_Answer):
        if user_answer.lower() == correct_Answer.lower():
            self.score += 1
            print("---That's Correct!!----")
            print(f"Your current score is {self.score}/{self.question_number}")
        else:
            print("---That's Wrong!!----")    
            print(f"The correct answer was {correct_Answer}.")
            print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
        

            