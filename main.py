import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
#Destroys current window and opens initial menu
def return_to_menu(window):
    window.destroy()
    menu()
def refresh_canvas(grid,window,size_x,size_y,size,space):
    window.destroy()
    visualize_grid_gin(grid,size_x,size_y,size,space)
#Draws Non Solved Grid
def visualize_grid_gin(grid,size_x,size_y,size,space):
    window = tk.Tk()
    window.title('Import Grid .gin')
    canvas = tk.Canvas(window,width= size_x*(space+size/2), height= size_y*(space+size/2),bg="white")
    for island in grid.keys():
        canvas.create_oval(space+grid[island][0]*space,space+grid[island][1]*space,space+(grid[island][0]*space)+size,space+(grid[island][1]*space)+size,outline="black",fill="white")
        canvas.create_text(space+grid[island][0]*space+size/2,space+grid[island][1]*space+size/2,text=grid[island][2],fill="black")
    canvas.pack()
    ttk.Label(text="Size").pack()
    scl_size = tk.Scale(from_=10,to=100,orient="horizontal")
    scl_size.set(size)
    scl_size.pack()
    ttk.Label(text="Spacing").pack()
    scl_space = tk.Scale(from_=10,to=100,orient="horizontal")
    scl_space.set(space)
    scl_space.pack()
    ttk.Button(text="Refresh",command=lambda: refresh_canvas(grid,window,size_x,size_y,scl_size.get(),scl_space.get())).pack()
    ttk.Button(text="Return To Menu",command=lambda: return_to_menu(window)).pack()
    
    window.mainloop()

def read_grid_from_file(window):
    #Load file
    file_name = askopenfilename(
        filetypes=[("Grid Input File", "*.gin")]
    )
    if not file_name:
        return
    file = open(file_name, "r")
    file_content = file.read()
    file_content = file_content.splitlines()
    #init grid
    grid = {}
    grid_size_x = int(file_content[0][0])
    grid_size_y = int(file_content[0][2])
    curr_available_id = 1

    #Load file to dict
    for j in range(1,grid_size_y+1):
        for i in range(0,grid_size_x):
            if file_content[j][i] != "0":
                grid[str(curr_available_id)] = [i,j-1,int(file_content[j][i]),[0,0,0,0]]
                curr_available_id += 1
    #dict format

    #grid = {'1': x,y,d,[up,down,left,right],...}

    #add aligned islands
    for island in grid.keys():
        for other_island in grid.keys():
            if island != other_island:
                #Check if x1=x2
                if grid[island][0] == grid[other_island][0]:
                    #Check if y1<y2
                    if grid[island][1] < grid[other_island][1] and grid[island][3][1] == 0:
                        grid[island][3][1] = other_island
                    #Check if y1>y2
                    elif grid[island][1] > grid[other_island][1] and grid[island][3][0] == 0:
                        grid[island][3][0] = other_island
                #Check if y1=y2
                elif grid[island][1] == grid[other_island][1]:
                    #Check if x1<x2
                    if grid[island][0] < grid[other_island][0] and grid[island][3][2] == 0:
                        grid[island][3][2] = other_island
                    #Check if x1>x2
                    elif grid[island][0] > grid[other_island][0] and grid[island][3][2] == 0:
                        grid[island][3][3] = other_island
    #Debug
    print(grid)
    file.close()
    #closes menu
    window.destroy()
    #Open Grid Visuals
    visualize_grid_gin(grid,grid_size_x,grid_size_y,50,75)

def menu():
    window = tk.Tk()
    window.title('Hashiwokakero')
    image_logo = ImageTk.PhotoImage(Image.open("static/logo.jpg"))
    lbl_logo = ttk.Label(image=image_logo)
    lbl_logo.pack()
    btn_convert_grid = ttk.Button(text="Import Grid To Test",command=lambda: read_grid_from_file(window))
    btn_convert_grid.pack()
    btn_sol_grid = ttk.Button(text="Import Grid Solution")
    btn_sol_grid.pack()
    lbl_menu = ttk.Label(text="Created by TAHA Anthony, HAJJ ASSAF Sam, FAWAZ Jad, EL CHAMAA Mohammad.")
    lbl_menu.pack()
    window.mainloop()

def main():
    menu()
main()