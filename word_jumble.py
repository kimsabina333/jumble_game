from tkinter import *
from tkinter import ttk
from random import choice, shuffle

# Global variables
current_topic = ""

def start_game(topic):
    global current_topic
    current_topic = topic
    game_frame.pack()
    shuffler(topic)
    start_button.config(state=DISABLED)

def shuffler(topic):
    hint_label.config(text='')
    global hint_count
    hint_count = 0
    entry_answer.set('')
    answer_label.config(text='')

    topics = {
        "fruits": ['алма', 'қауын', 'анар', 'қарбыз', 'шабдалы'],
        "family": ['ата', 'ана', 'бала', 'қыз', 'еш', 'әже'],
        "human": ['үй', 'ауыз', 'башпай', 'бас', 'шаш', 'өкпе']
    }

    global word
    word = choice(topics[topic])
    break_apart_word = list(word)
    shuffle(break_apart_word)
    global shuffled_word
    shuffled_word = ''
    for letter in break_apart_word:
        shuffled_word += letter
    my_label.config(text=shuffled_word)

def answer():
    if word == entry_answer.get():
        answer_label.config(text="Correct answer!", fg='green')
    else:
        answer_label.config(text="Wrong answer, please try again.", fg='red')

def hint():
    global hint_count
    word_length = len(word)
    if hint_count < word_length:
        hint_label.config(text=f'{hint_label["text"]} {word[hint_count]}')
        hint_count += 1

def exit_game():
    root.destroy()

root = Tk()
root.title('Word Jumble Game')
root.geometry("700x500")

# Create menu
menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=exit_game)

# Game Frame
game_frame = Frame(root)

my_label = Label(game_frame, text="", font=("Arial", 48), )
my_label.pack(pady=20)

entry_answer = ttk.Combobox(game_frame, font=("Arial", 24), values=list('әіңғүұқ'))
entry_answer.pack(pady=20)
button_frame = Frame(game_frame)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=answer, bg='orange', width=8, font=("Arial", 10))
answer_button.grid(row=0, column=0, padx=10)
my_button = Button(button_frame, text="Pick Another Word", command=lambda: shuffler(current_topic), bg='orange', width=15, font=("Arial", 10))
my_button.grid(row=0, column=1, padx=10)
hint_button = Button(button_frame, text="Hint", command=lambda: hint(), bg='orange', width=5, font=("Arial", 10))
hint_button.grid(row=0, column=2, padx=10)

answer_label = Label(game_frame, text='', font=("Arial", 22))
answer_label.pack(pady=20)
hint_label = Label(game_frame, text='', font=("Arial", 22))
hint_label.pack(pady=10)

start_button = Button(root, text="Start Game", command=lambda: topic_selection.pack(), bg='orange', width=15, font=("Arial", 10))
start_button.pack(pady=20)

# Topic Selection Frame
topic_selection = Frame(root)

fruits_button = Button(topic_selection, text="Fruits", command=lambda: start_game("fruits"), bg='orange', width=10, font=("Arial", 10))
fruits_button.grid(row=0, column=0, padx=10, pady=10)
family_button = Button(topic_selection, text="Family", command=lambda: start_game("family"), bg='orange', width=10, font=("Arial", 10))
family_button.grid(row=0, column=1, padx=10, pady=10)
home_button = Button(topic_selection, text="Human", command=lambda: start_game("human"), bg='orange', width=10, font=("Arial", 10))
home_button.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()
