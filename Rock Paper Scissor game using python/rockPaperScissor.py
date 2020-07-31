import random
import tkinter

stats = list()

# defining a function to check the winner, computer calls and append the stats
def get_winner(call) :
    if random.random() <= (1/3) :
        throw = "rock"
    elif (1/3) < random.random() <= (2/3) :
        throw = "paper"
    else :
        throw = "scissor"
    if (throw == "rock" and call == "paper") or (throw == "paper" and call == "scissor") or (throw == "scissor" and call == "rock") :
        stats.append("W")
        result = "You won :)"
    elif (throw == call) :
        stats.append("D")
        result = "It's a draw"
    else :
        stats.append("L")
        result = "You lost :("
    global output
    output.config(text="Computer did: " + throw + "\n" + result)

# defining function to take user calls
def pass_s() :
    get_winner("scissor")
def pass_r() :
    get_winner("rock")
def pass_p() :
    get_winner("paper")

# creating buttons to use functions
win = tkinter.Tk()

scissor = tkinter.Button(win, text = "Scissor", bg = "#ff9999", padx = 5, pady = 10, command = pass_s, width = 30)
rock = tkinter.Button(win, text = "Rock", bg = "#80ff80", padx = 5, pady = 10, command = pass_r, width = 30)
paper = tkinter.Button(win, text = "Paper", bg = "#3399ff", padx = 5, pady = 10, command = pass_p, width = 30)
output = tkinter.Label(win, text = "What's your call ?", width = 30, fg = "red")

# placing buttons
scissor.pack(side = "left")
rock.pack(side = "left")
paper.pack(side = "left")
output.pack(side = "right")
win.mainloop()

# whether you lost or won the series
print("Results of each game are as follows : ")

for i in stats :
    print(i)
if stats.count("L") > stats.count("W") :
    print("You lost the series :(")
elif stats.count("L") < stats.count("W") :
    print("You won the series :)")
else :
    print("The series ended in a draw")
        
        
