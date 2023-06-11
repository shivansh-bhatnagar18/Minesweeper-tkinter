import customtkinter
import random

def first_click_of_the_game(index):
    global map, rows, columns, bombs, matrix, flags_remaining
    map=["💣" for i in range(bombs)]+[" " for i in range(rows*columns-bombs)]
    random.shuffle(map)
    while(map[index]=="💣"):
        random.shuffle(map)
    for i in range(rows*columns):
        matrix[i].configure(command= lambda x=i: click_button(x))
        matrix[i].bind('<Button-3>', lambda eff, x=i: rightclick(event=eff, index=x))
    click_button(index)

def click_button(index):
    global map, rows, columns, bombs, matrix, flags_remaining, flag_map, reached, live_stack, flags, is_game_over, game_status
    if (index in flag_map or is_game_over or index in reached):
        return
    if map[index]=="💣":
        game_status.configure(text="Game Status : You Lost")
        game_over()
        return
    live_stack.append(index)
    while len(live_stack)>0:
        current_index=live_stack[-1]
        current_value=value_of_the_button(current_index)
        reached.append(current_index)
        live_stack.pop()
        if current_value==0:
            for i in neighbourhood(current_index):
                if i not in reached and i not in live_stack:
                    live_stack.append(i)
            matrix[current_index].configure(fg_color="cyan")
        else:
            matrix[current_index].configure(text=str(current_value))
        for i in flag_map:
            if i in reached:
                matrix[i].config(text=" ")
                flags+=1
                flag_map.remove(i)
        if(len(reached)==rows*columns-bombs):
            print("You Won")
            game_status.configure(text="Game Status : You Won")
            game_over()

def neighbourhood(index):
    global rows,columns
    elements=[]
    for col in [-columns,0,columns]:
        if index+col<0 or (index+col)>=(rows*columns):
            continue
        for i in [-1,0,1]:
            if index//columns != (index+i)//columns:
                continue
            elements.append(index+col+i)
    elements.remove(index)
    return elements

def value_of_the_button(index):
    count=0
    for i in neighbourhood(index):
        if map[i]=="💣":
            count+=1
    return count

def game_over():
    global is_game_over, rows, columns, game_status
    is_game_over=True
    for i in range(rows*columns):
        if map[i]=="💣":
            matrix[i].configure(text="💣")


def rightclick(event,index):
    global flag_map, reached, matrix, flags, is_game_over, flagsLabel
    if index in reached or is_game_over:
        return
    if index in flag_map:
        matrix[index].configure(text="️‍️‍ ", fg_color="Grey")
        flags+=1
        flagsLabel.configure(text= f"Flags : {flags}")
        flag_map.remove(index)
    elif flags>0:
        matrix[index].configure(fg_color="red")
        flags-=1
        flagsLabel.configure(text=f"Flags : {flags}")
        flag_map.append(index)


def easy_game():
    global matrix, rows, columns, bombs, live_stack, reached, flag_map, is_game_over, flags, flagsLabel, game_status
    easy_game_window = customtkinter.CTk()
    easy_game_window.geometry("600x400")
    easy_game_window.title("Easy Game Minesweeper")
    easy_game_window.resizable(False, False)

    upper_bar=customtkinter.CTkFrame(easy_game_window, width=600, height=50, fg_color="#808080")
    upper_bar.place(relx=0, rely=0)

    easy_grid=customtkinter.CTkFrame(easy_game_window, width=360, height=300, fg_color="#808080" )
    easy_grid.place(x=120,y=90)

    live_stack = []
    reached = []
    flag_map = []
    matrix = []
    rows=5
    columns=6
    bombs=5
    flags=bombs
    is_game_over=False


    flagsLabel=customtkinter.CTkLabel(upper_bar, text=f"Flags : {flags}", text_color="Black", font=("SF Atarian System",40))
    flagsLabel.place(x=450,y=10)

    game_status=customtkinter.CTkLabel(upper_bar, text=f"Game Status : -", text_color="Black", font=("SF Atarian System",40))
    game_status.place(x=10,y=10)


    for i in range(rows*columns):
        matrix.append(customtkinter.CTkButton(easy_grid, width=60, height=60, text=" ", hover=True,
                                    fg_color="#808080", corner_radius=5, border_color="black",border_width=2,
                                    text_color="black", font=("SF Atarian System",25), command= lambda x=i: first_click_of_the_game(x)))
        matrix[i].grid(row=i//columns, column=i%columns)

    easy_game_window.mainloop()

def medium_game():
    global matrix, rows, columns, bombs, live_stack, reached, flag_map, is_game_over, flags, flagsLabel, game_status
    medium_game_window = customtkinter.CTk()
    medium_game_window.geometry("600x400")
    medium_game_window.title("Medium Game Minesweeper")
    medium_game_window.resizable(False, False)

    upper_bar = customtkinter.CTkFrame(medium_game_window, width=600, height=50, fg_color="#808080")
    upper_bar.place(relx=0, rely=0)

    easy_grid = customtkinter.CTkFrame(medium_game_window, width=360, height=300, fg_color="#808080")
    easy_grid.place(x=120, y=90)

    live_stack = []
    reached = []
    flag_map = []
    matrix = []
    rows = 10
    columns = 12
    bombs = 20
    flags = bombs
    is_game_over = False

    flagsLabel=customtkinter.CTkLabel(upper_bar, text=f"Flags : {flags}", text_color="Black", font=("SF Atarian System",40))
    flagsLabel.place(x=450,y=10)

    game_status=customtkinter.CTkLabel(upper_bar, text=f"Game Status : -", text_color="Black", font=("SF Atarian System",40))
    game_status.place(x=10,y=10)

    for i in range(rows * columns):
        matrix.append(customtkinter.CTkButton(easy_grid, width=30, height=30, text=" ", hover=True,
                                              fg_color="#808080", corner_radius=5, border_color="black", border_width=1.5,
                                              text_color="black", font=("SF Atarian System", 20),
                                              command=lambda x=i: first_click_of_the_game(x)))
        matrix[i].grid(row=i // columns, column=i % columns)

    medium_game_window.mainloop()

def hard_game():
    global matrix, rows, columns, bombs, live_stack, reached, flag_map, is_game_over, flags, flagsLabel, game_status
    hard_game_window = customtkinter.CTk()
    hard_game_window.geometry("600x450")
    hard_game_window.title("Hard Game Minesweeper")
    hard_game_window.resizable(False, False)

    upper_bar = customtkinter.CTkFrame(hard_game_window, width=600, height=50, fg_color="#808080")
    upper_bar.place(relx=0, rely=0)

    easy_grid = customtkinter.CTkFrame(hard_game_window, width=360, height=300, fg_color="#808080")
    easy_grid.place(x=120, y=90)

    live_stack = []
    reached = []
    flag_map = []
    matrix = []
    rows = 15
    columns = 18
    bombs = 30
    flags = bombs
    is_game_over = False

    flagsLabel=customtkinter.CTkLabel(upper_bar, text=f"Flags : {flags}", text_color="Black", font=("SF Atarian System",40))
    flagsLabel.place(x=450,y=10)

    game_status=customtkinter.CTkLabel(upper_bar, text=f"Game Status : -", text_color="Black", font=("SF Atarian System",40))
    game_status.place(x=10,y=10)

    for i in range(rows * columns):
        matrix.append(customtkinter.CTkButton(easy_grid, width=20, height=20, text=" ", hover=True,
                                              fg_color="#808080", corner_radius=5, border_color="black", border_width=2,
                                              text_color="black", font=("SF Atarian System", 15),
                                              command=lambda x=i: first_click_of_the_game(x)))
        matrix[i].grid(row=i // columns, column=i % columns)

    hard_game_window.mainloop()


current_main = customtkinter.CTk()
current_main.geometry("600x400")
current_main.title("Minesweeper")
current_main.resizable(False,False)

customtkinter.set_appearance_mode("Dark")

minesweeper_heading = customtkinter.CTkLabel(master=current_main, text="Minesweeper", font=("SF Atarian System",50))
minesweeper_heading.place(x=200,y=50)

select_difficulty = customtkinter.CTkLabel(master=current_main, text="Please Select the Difficulty", font=("SF Atarian System",35))
select_difficulty.place(x=140,y=130)

button_easy = customtkinter.CTkButton(master=current_main, fg_color="#0F3460", text="Easy", font=("SF Atarian System",30), command=easy_game)
button_medium = customtkinter.CTkButton(master=current_main, fg_color="#0F3460", text="Medium", font=("SF Atarian System",30), command=medium_game)
button_hard = customtkinter.CTkButton(master=current_main, fg_color="#0F3460", text="Hard", font=("SF Atarian System",30), command=hard_game)
button_easy.place(x=230,y=210)
button_medium.place(x=230,y=250)
button_hard.place(x=230,y=290)

current_main.mainloop()


