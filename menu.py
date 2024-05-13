import tkinter as tk
import subprocess

def play_two_players():
    print("Играем с игроком")
    subprocess.Popen(["python", "game_two_players.py"])

def play_with_bot():
    print("Играем с ботом")
    subprocess.Popen(["python", "game_bot.py"])

def exit_game():
    root.destroy()

# Создаем главное окно
root = tk.Tk()
root.title("Главное меню")
root.geometry("1000x1000")

title_label = tk.Label(root, text="Дартс", font=("Helvetica", 24))
title_label.pack(pady=50)

# Функции для кнопок
play_two_players_button = tk.Button(root, text="Играть вдвоем", command=play_two_players, height=3, width=20)
play_two_players_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

play_with_bot_button = tk.Button(root, text="Играть с ботом", command=play_with_bot, height=3, width=20)
play_with_bot_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

exit_button = tk.Button(root, text="Выход", command=exit_game, height=3, width=20)
exit_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

root.mainloop()
