from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class Ui:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.score_label = Label(text=f"Score: 0", fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.questions= self.canvas.create_text(150,125,text="some questions",fill=THEME_COLOR,font=("Ariel",20,"italic"),width=280)
        self.canvas.config(highlightthickness=0,)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        right_image = PhotoImage(file="/Users/anirudhmulky/Desktop/python/quizzler-app-start/images/true.png")
        
        wrong_image = PhotoImage(file="/Users/anirudhmulky/Desktop/python/quizzler-app-start/images/false.png")
        self.true_button = Button(image=right_image,highlightthickness=0,command=self.true)
        self.true_button.grid(row=2,column=0)
        self.false_button = Button(image=wrong_image,highlightthickness=0,command=self.false)
        self.false_button.grid(row=2,column=1)

        self.get_que()

        self.window.mainloop()
    
    def get_que(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questions, text = q_text)
            
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.questions, text="You have reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_que)

