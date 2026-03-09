import tkinter as tk

# Create window
root = tk.Tk()
root.title("Adventure Game")
root.geometry("500x350")
root.resizable(False, False)

# Load background images
forest_bg = tk.PhotoImage(file="forest.png")
cave_bg = tk.PhotoImage(file="cave.png")
river_bg = tk.PhotoImage(file="river.png")

# Background label
background = tk.Label(root)
background.place(x=0, y=0, relwidth=1, relheight=1)

# Story text
story = tk.Label(
    root,
    text="",
    wraplength=400,
    font=("Arial", 12),
    bg="black",
    fg="white"
)
story.pack(pady=40)

# Buttons
button1 = tk.Button(
    root,
    width=20,
    font=("Arial", 11)
)
button1.pack(pady=5)

button2 = tk.Button(
    root,
    width=20,
    font=("Arial", 11)
)
button2.pack(pady=5)


# Win scene
def win():
    story.config(text="You win! You found treasure and survived the adventure.")
    
    button1.config(text="Play Again", command=start_game)
    button2.config(text="Exit", command=root.quit)


# Lose scene
def lose():
    story.config(text="Game Over. Your adventure ends here.")
    
    button1.config(text="Play Again", command=start_game)
    button2.config(text="Exit", command=root.quit)


# Cave path
def cave():
    background.config(image=cave_bg)

    story.config(text="You entered the cave. A monster appears!")
    
    button1.config(text="Fight the monster", command=win)
    button2.config(text="Run away", command=lose)


# River path
def river():
    background.config(image=river_bg)

    story.config(text="You reached a strong river.")
    
    button1.config(text="Swim across", command=lose)
    button2.config(text="Walk along the river", command=win)


# Start scene
def start_game():
    background.config(image=forest_bg)

    story.config(text="You are standing in a dark forest. Two paths lie ahead.")
    
    button1.config(text="Enter the cave", command=cave)
    button2.config(text="Go to the river", command=river)


# Start the game
start_game()

# Run GUI
root.mainloop()