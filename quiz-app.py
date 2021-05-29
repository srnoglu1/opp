import random
class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer


    def checkAnswer(self,answer):
        if answer not in self.choices:
            raise ValueError("incorrect entry")
        return self.answer == answer

  
class Quiz:
    def __init__(self,questions):
        self.questions = random.sample(questions, len(questions))
        self.questionIndex = 0
        self.score = 0


    def getQuestion(self):
        return self.questions[self.questionIndex]


    def displayQuestion(self):
        question = self.getQuestion()
  
        print(f"Question {self.questionIndex + 1}: {question.text}")

        for q in question.choices:
            print("*" , q)

        answer = input("Answer: ")
        if (question.checkAnswer(answer)):
            self.score += 1
            print("your answer is correct.")

        self.questionIndex += 1
        self.loadQuestion()


    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            print(self.score)
        else:
            self.displayProgress()
            self.displayQuestion()    


    def displayScore(self):
        print("your test result".center(50,'*'))
        point = 100 / len(self.questions)
        totalPoint = round(self.score * point)
        print("Score:",totalPoint)
        

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        print(f"You are in questions {totalQuestion} of {questionNumber}.questions.")


q1 = Question("What is the best programming language ?",["python","java","dart"],"python")
q2 = Question("Which is the easiest programming language ?",["python","java","dart"],"python")
q3 = Question("What is the most popular programming language ?",["python","java","dart"],"python")


_questions = [q1,q2,q3]

quiz = Quiz(_questions)

print(quiz.loadQuestion())
