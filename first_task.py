import tkinter as tk
import random


def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-'])
    question = f"Решите пример: {num1} {operator} {num2}" + " = "
    if operator == '+':
        result = num1 + num2
    else:
        result = num1 - num2
    return question, result


def check_answer():
    user_answer = entry.get()
    if user_answer == str(result):
        label.config(text="Отлично! Ответ правильный!")
    else:
        label.config(text="Неправильно! Попробуйте ещё раз!")


def next_question():
    global result
    question, result = generate_question()
    question_label.config(text=question)
    entry.delete(0, 'end')
    label.config(text="")


root = tk.Tk()
root.title("Проверка умения складывать и вычитать")
root.geometry("500x300")
root["bg"] = "#a7c3cf"

question_label = tk.Label(root, text="", font=(
    "Arial", 20), background="#a7c3cf")
question_label.pack()

entry = tk.Entry(root, font=("Arial", 24))
entry.pack()

check_button = tk.Button(root, text="Проверить ответ", font=(
    "Arial", 20, 'bold'),  bg="#a7c3cf", command=check_answer)
check_button.pack(anchor="center", padx=20, pady=30)

label = tk.Label(root, text="", font=("Arial", 16), background="#a7c3cf")
label.pack(padx=20, pady=0)

next_button = tk.Button(root, text="Следующий пример",
                        font=("Arial", 18), bg="#679fb8", command=next_question)
next_button.pack(anchor="s", padx=10, pady=20)

next_question()

root.mainloop()
