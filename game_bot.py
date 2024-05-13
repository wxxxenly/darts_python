import tkinter
import math
import random

log_file = open("dart_bot_log.log", "a")

# Create the window
root = tkinter.Tk()
root.title("Darts Game")
root.geometry("1000x1000")

frame = tkinter.Frame(root)
scroll_bar = tkinter.Scrollbar(frame, orient=tkinter.VERTICAL)

listbox = tkinter.Listbox(frame, width=25, yscrollcommand=scroll_bar.set)

scroll_bar.config(command=listbox.yview)
scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
frame.pack(side=tkinter.TOP)

listbox.pack(pady=15)

def exit_game():
    root.destroy()

# Create the canvas
canvas = tkinter.Canvas(root, width=600, height=600)
canvas.pack()

# Draw the dartboard
canvas.create_oval(0, 0, 600, 600, outline="black", width=1, fill="green")
canvas.create_oval(50, 50, 550, 550, outline="black", width=1, fill="red")
canvas.create_oval(100, 100, 500, 500, outline="black", width=1, fill="green")
canvas.create_oval(150, 150, 450, 450, outline="black", width=1, fill="red")

for i in range(20):
    x1 = 300  # coordinates of the circle center
    y1 = 300
    angle = i * 18  # angle between the lines
    x2 = 300 + 300 * math.cos(math.radians(angle))  # find the coordinates of the line end
    y2 = 300 + 300 * math.sin(math.radians(angle))
    
    canvas.create_line(x1, y1, x2, y2, fill="black", width=2)
    

canvas.create_oval(200, 200, 400, 400, outline="black", width=1, fill="green")
canvas.create_oval(250, 250, 350, 350, outline="black", width=5, fill="red")

# Function to calculate score
def calculate_score(x, y):
    
    distance = ((x - 300) ** 2 + (y - 300) ** 2) ** 0.5
    if distance <= 50:
        return 50
    elif distance <= 100:
        return 25
    elif distance <= 150:
        if y>300 and x>300:
            if y<0.325*x+202.524:
                return 6
        
            elif y>0.325*x+202.524 and y<0.727*x+82.0372416:
                return 10
        
            elif y>0.726542528*x+82.0372416 and y<1.376*x-112.913:
                return 15
        
            elif y>1.376*x-112.913 and y<3.078*x-623.306:
                return 2
        
            elif y>3.078*x-623.306:
                return 17
        
        elif x<300 and y>300:
            if y>-3.078*x+1223.306:
                return 3
            elif y>-1.37638192*x+712.9145761 and y<-3.078*x+1223.306:
                return 19
        
            elif y>-0.726542528*x+517.9627584 and y<-1.37638192*x+712.9145761:
                 return 7
        
            elif y>-0.324919696*x+397.4759089 and y<-0.726542528*x+517.9627584:
                return 16
        
            elif y<-0.324919696*x+397.4759089:
                return 8
        
        
        elif x<300 and y<300:
            if y>0.324919696*x+202.5240911 :
                return 11
        
            elif y>0.726542528*x+82.0372416 and y<0.324919696*x+202.5240911:
                return 14
        
            elif y>1.37638192*x-112.9145761 and y<0.726542528*x+82.0372416:
                return 9
        
            elif y>3.077683537*x-623.3050612 and y<1.37638192*x-112.9145761:
                return 12
        
            elif y<3.077683537*x-623.3050612:
                return 5
        elif x>300 and y<300:
            if y<-3.077683537*x+1223.305061 :
                return 20
        
            elif  y<-1.37638192*x+712.9145761 and y>-3.077683537*x+1223.305061:
                return 1
        
            elif y<-0.726542528*x+517.9627584 and y>-1.37638192*x+712.9145761:
                return 18
        
            elif y<-0.324919696*x+397.4759089 and y>-0.726542528*x+517.9627584:
                return 4
        
            elif y>-0.324919696*x+397.4759089:
                return 13
        





    elif distance <= 200:
        if y>300 and x>300:
            if y<0.325*x+202.524:
                return 6*3
        
            elif y>0.325*x+202.524 and y<0.727*x+82.0372416:
                return 10*3
        
            elif y>0.726542528*x+82.0372416 and y<1.376*x-112.913:
                return 15*3
        
            elif y>1.376*x-112.913 and y<3.078*x-623.306:
                return 2*3
        
            elif y>3.078*x-623.306:
                return 17*3
        
        elif x<300 and y>300:
            if y>-3.078*x+1223.306:
                return 3*3
            elif y>-1.37638192*x+712.9145761 and y<-3.078*x+1223.306:
                return 19*3
        
            elif y>-0.726542528*x+517.9627584 and y<-1.37638192*x+712.9145761:
                 return 7*3
        
            elif y>-0.324919696*x+397.4759089 and y<-0.726542528*x+517.9627584:
                return 16*3
        
            elif y<-0.324919696*x+397.4759089:
                return 8*3
        
        
        elif x<300 and y<300:
            if y>0.324919696*x+202.5240911 :
                return 11*3
        
            elif y>0.726542528*x+82.0372416 and y<0.324919696*x+202.5240911:
                return 14*3
        
            elif y>1.37638192*x-112.9145761 and y<0.726542528*x+82.0372416:
                return 9*3
        
            elif y>3.077683537*x-623.3050612 and y<1.37638192*x-112.9145761:
                return 12*3
        
            elif y<3.077683537*x-623.3050612:
                return 5*3
        elif x>300 and y<300:
            if y<-3.077683537*x+1223.305061 :
                return 20*3
        
            elif  y<-1.37638192*x+712.9145761 and y>-3.077683537*x+1223.305061:
                return 1*3
        
            elif y<-0.726542528*x+517.9627584 and y>-1.37638192*x+712.9145761:
                return 18*3
        
            elif y<-0.324919696*x+397.4759089 and y>-0.726542528*x+517.9627584:
                return 4*3
        
            elif y>-0.324919696*x+397.4759089:
                return 13*3
    elif distance <= 250:
        if y>300 and x>300:
            if y<0.325*x+202.524:
                return 6
        
            elif y>0.325*x+202.524 and y<0.727*x+82.0372416:
                return 10
        
            elif y>0.726542528*x+82.0372416 and y<1.376*x-112.913:
                return 15
        
            elif y>1.376*x-112.913 and y<3.078*x-623.306:
                return 2
        
            elif y>3.078*x-623.306:
                return 17
        
        elif x<300 and y>300:
            if y>-3.078*x+1223.306:
                return 3
            elif y>-1.37638192*x+712.9145761 and y<-3.078*x+1223.306:
                return 19
        
            elif y>-0.726542528*x+517.9627584 and y<-1.37638192*x+712.9145761:
                 return 7
        
            elif y>-0.324919696*x+397.4759089 and y<-0.726542528*x+517.9627584:
                return 16
        
            elif y<-0.324919696*x+397.4759089:
                return 8
        
        
        elif x<300 and y<300:
            if y>0.324919696*x+202.5240911 :
                return 11
        
            elif y>0.726542528*x+82.0372416 and y<0.324919696*x+202.5240911:
                return 14
        
            elif y>1.37638192*x-112.9145761 and y<0.726542528*x+82.0372416:
                return 9
        
            elif y>3.077683537*x-623.3050612 and y<1.37638192*x-112.9145761:
                return 12
        
            elif y<3.077683537*x-623.3050612:
                return 5
        elif x>300 and y<300:
            if y<-3.077683537*x+1223.305061 :
                return 20
        
            elif  y<-1.37638192*x+712.9145761 and y>-3.077683537*x+1223.305061:
                return 1
        
            elif y<-0.726542528*x+517.9627584 and y>-1.37638192*x+712.9145761:
                return 18
        
            elif y<-0.324919696*x+397.4759089 and y>-0.726542528*x+517.9627584:
                return 4
        
            elif y>-0.324919696*x+397.4759089:
                return 13
            else:
                return 0
    elif distance <= 350:
        if y>300 and x>300:
            if y<0.325*x+202.524:
                return 6*2
        
            elif y>0.325*x+202.524 and y<0.727*x+82.0372416:
                return 10*2
        
            elif y>0.726542528*x+82.0372416 and y<1.376*x-112.913:
                return 15*2
        
            elif y>1.376*x-112.913 and y<3.078*x-623.306:
                return 2*2
        
            elif y>3.078*x-623.306:
                return 17*2
            else:
                return 0
        
        elif x<300 and y>300:
            if y>-3.078*x+1223.306:
                return 3*2
            elif y>-1.37638192*x+712.9145761 and y<-3.078*x+1223.306:
                return 19*2
        
            elif y>-0.726542528*x+517.9627584 and y<-1.37638192*x+712.9145761:
                 return 7*2
        
            elif y>-0.324919696*x+397.4759089 and y<-0.726542528*x+517.9627584:
                return 16*2
        
            elif y<-0.324919696*x+397.4759089:
                return 8*2
        
        
        elif x<300 and y<300:
            if y>0.324919696*x+202.5240911 :
                return 11*2
        
            elif y>0.726542528*x+82.0372416 and y<0.324919696*x+202.5240911:
                return 14*2
        
            elif y>1.37638192*x-112.9145761 and y<0.726542528*x+82.0372416:
                return 9*2
        
            elif y>3.077683537*x-623.3050612 and y<1.37638192*x-112.9145761:
                return 12*2
        
            elif y<3.077683537*x-623.3050612:
                return 5*2
            else:
                return 0
        elif x>300 and y<300:
            if y<-3.077683537*x+1223.305061 :
                return 20*2
        
            elif  y<-1.37638192*x+712.9145761 and y>-3.077683537*x+1223.305061:
                return 1*2
        
            elif y<-0.726542528*x+517.9627584 and y>-1.37638192*x+712.9145761:
                return 18*2
        
            elif y<-0.324919696*x+397.4759089 and y>-0.726542528*x+517.9627584:
                return 4*2
        
            elif y>-0.324919696*x+397.4759089:
                return 13*2
            else:
                return 0
        else:
            return 0
    else:
        return 0
        
def log_player(score):
    log_file.write(f"Player: {score}\n")
    randomX = random.randint(0, 600)
    randomY = random.randint(0, 600)
    botClick(randomX, randomY)
    listbox.insert(tkinter.END, f"")
        
def log_bot(score):
    log_file.write(f"Bot: {score}\n")

# Function for mouse click
def click(event):
    x = event.x
    y = event.y

    # Рисуем крестик в новом местоположении
    canvas.create_line(x - 10, y - 10, x + 10, y + 10, fill="black", tags="cross")
    canvas.create_line(x + 10, y - 10, x - 10, y + 10, fill="black", tags="cross")

    score = calculate_score(x, y)
    player_scores.append([score, 'Player'])
    update_scores()
    log_player(score)

# Function for mouse click
def botClick(x, y):    
    # Рисуем крестик в новом местоположении
    canvas.create_line(x - 10, y - 10, x + 10, y + 10, fill="black", tags="cross")
    canvas.create_line(x + 10, y - 10, x - 10, y + 10, fill="black", tags="cross")

    score = calculate_score(x, y)
    player_scores.append([score, 'Bot'])
    update_scores()
    log_bot(score)
    

# Function to update score display
def update_scores():
    listbox.insert(tkinter.END, f"{player_scores[-1][1]}: {player_scores[-1][0]}")    
    score_player = sum([x[0] for x in player_scores if x[1] == 'Player'])
    score_bot = sum([x[0] for x in player_scores if x[1] == 'Bot'])
    
    player_score_display = tkinter.Label(root, text=f"Player Score\n {score_player}", font=("Helvetica", 16))
    player_score_display.place(x=120, y=20)
    player_score_display.config()
    
    bot_score_display = tkinter.Label(root, text=f"Bot Score\n {score_bot}", font=("Helvetica", 16))
    bot_score_display.config()
    bot_score_display.place(x=750, y=20)
            

exit_button = tkinter.Button(root, text="Выход", command=exit_game, height=3, width=20)
exit_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

# Get the number of players from the console
num_players = 2
player_scores = []

# Bind the function to the mouse click event
canvas.bind("<Button-1>", click)

# Display the player score
player_score_display = tkinter.Label(root, text="Player Score\n 0", font=("Helvetica", 16))
player_score_display.place(x=120, y=20)

# Display the bot score
bot_score_display = tkinter.Label(root, text="Bot Score\n 0", font=("Helvetica", 16))
bot_score_display.place(x=750, y=20)

# Start the game
root.mainloop()
