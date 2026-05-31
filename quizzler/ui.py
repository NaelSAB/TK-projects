from logging import disable
from tkinter import *

from numpy.ma.core import true_divide

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        #window:
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        #image:
        self.true_image = PhotoImage(file="./images/true.png")
        self.false_image = PhotoImage(file="./images/false.png")

        #labels:
        self.label_score = Label(text="Score: 0", background=THEME_COLOR, fg="white")
        self.label_score.grid(column=1, row=0)

        #canves:
        self.canves = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canves.create_text(150, 125, width=280, text="question", fill=THEME_COLOR, font=FONT)
        self.canves.grid(column=0, row=1, columnspan=2, pady=50)

        #buttons:
        self.true_button = Button(image=self.true_image, highlightthickness=0, borderwidth=0, activebackground=THEME_COLOR, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=self.false_image, highlightthickness=0, borderwidth=0, activebackground=THEME_COLOR, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canves.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.label_score.config(text=f"Score: {self.quiz.score}")
            self.canves.itemconfig(self.question_text, text= q_text)
        else:
            self.canves.itemconfig(self.question_text, text= "You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canves.config(bg="green")
        else:
            self.canves.config(bg="red")
        self.window.after(1000, self.get_next_question)