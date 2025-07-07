import tkinter as tk
from tkinter import messagebox
from quiz_manager import QuizManager

# Initialize QuizManager with questions.json
quiz = QuizManager("questions.json")

# Function to handle answer selection
def handle_answer(selected_option):
    is_correct = quiz.check_answer(selected_option)
    if is_correct:
        messagebox.showinfo("Result", "Correct!")
    else:
        messagebox.showinfo("Result", "Incorrect!")
    display_next_question()

# Function to display the next question
def display_next_question():
    question_data = quiz.get_next_question()
    if question_data:
        question_label.config(text=question_data["question"])
        for i, (key, option_text) in enumerate(question_data["options"].items()):
            option_buttons[i].config(text=f"{key}: {option_text}", command=lambda opt=key: handle_answer(opt))
    else:
        messagebox.showinfo("Quiz Complete", f"Your score is {quiz.score} out of {len(quiz.questions)}")
        root.quit()

# Set up the main Tkinter window
root = tk.Tk()
root.title("Quiz Game")

# Create a label for the question
question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=400)
question_label.pack(pady=20)

# Create buttons for options
option_buttons = []
for i in range(4):
    button = tk.Button(root, text="", width=20, font=("Arial", 12), command=lambda opt=i: handle_answer(opt))
    button.pack(pady=5)
    option_buttons.append(button)

# Display the first question
display_next_question()

root.mainloop()
