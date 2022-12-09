naziya = "naziya"

from email.mime import image
import os
from textwrap import fill
import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser,messagebox, filedialog
from PIL import Image


# os.chdir(r"D:\apk\exe")
# print(os.getcwd())

naziya = tk.Tk()
# naziya.geometry("1100x600")
# Gets the requested values of the height and widht.
windowWidth = naziya.winfo_reqwidth()
windowHeight = naziya.winfo_reqheight()
# print("Width",windowWidth,"Height",windowHeight)
 
# Gets both half the screen width/height and window width/height
positionRight = int(naziya.winfo_screenwidth()/2 - windowWidth*1.68)
positionDown = int(naziya.winfo_screenheight()/2 - windowHeight*1.68)
 
# Positions the window in the center of the page.
naziya.geometry("1100x600+{}+{}".format(positionRight-215, positionDown))
naziya.title("Naz Text Editor")
naziya.state("zoomed")
naziya.iconbitmap(r"D:\XD Course\Adobe Prototype\Naz text editor icon (3).ico")
naziya.configure(bg="#ffffff")

# *********************************** Main Menu **********************************
# MAIN MENU BAR
main_menu = tk.Menu(naziya, bg='black' , fg="white")





                                    # FUNCTION


# FUNCTION DEFINE FOR COLOR THEME
def lightdefault():
    text_editor.config(bg="#ffffff",fg="#000000")
    # status_bar_bottom.configure(bg="#ffffff",fg="#000000")
    

def lightplus():
    text_editor.config(bg="#c4c4c4",fg="#000000")
    # status_bar_bottom.configure(bg="#c4c4c4",fg="#000000")

def darktheme():
    text_editor.config(bg="#484848",fg="#ffffff")
    # status_bar_bottom.configure(bg="#484848",fg="#ffffff")

def monokaitheme():
    text_editor.config(bg="#d3b774",fg="#000000")
    # status_bar_bottom.configure(bg="#d3b774",fg="#000000")

def nightbluetheme():
    text_editor.config(bg="#447CF4",fg="#ffffff")
    # status_bar_bottom.configure(bg="#447CF4",fg="#ffffff")

def redtheme():
    text_editor.config(bg="#FEADAD",fg="#000000")
    # status_bar_bottom.configure(bg="#FEADAD",fg="#000000")

functiontuple = (lightdefault, lightplus ,darktheme ,monokaitheme , nightbluetheme ,redtheme)


# FUNCTION FOR ABOUT SECTION
def about_function():
    messagebox.showinfo("About" , "v1.0\nThis is Naz Text Editor Developed By Subhan Ali For ......❤")

def help_function():
    messagebox.showinfo("Help","For Reporting any type of bug/issue, you can report me on telegram @subhan7786")




# For File Section

file = tk.Menu(main_menu ,tearoff=False)
# importing icon
new_icon = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\new.png")
open_icon = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\open.png")
save_icon = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\save.png")
save_as_icon = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\save_as.png")
exit_icon = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\exit.png")


# For Edit Section

edit = tk.Menu(main_menu ,tearoff=False)
# importing icon
cut_icon = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\cut.png")
copy_icon = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\copy.png")
paste_icon = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\paste.png")
clear_all_icon = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\clear_all.png")
find_icon = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\find.png")


# For View Section

view = tk.Menu(main_menu ,tearoff=False)
# importing icon
status_bar = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\status_bar.png")
tool_bar = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\tool_bar.png")


# For Color Theme Section

colortheme = tk.Menu(main_menu ,tearoff=False)
# importing icon
light_default = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\light_default.png")
light_plus = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\light_plus.png")
dark = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\dark.png")
monokai = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\monokai.png")
night_blue = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\night_blue.png")
red = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\red.png")

theme_choice = tk.StringVar()
color_icon = (light_default, light_plus, dark, monokai, night_blue, red)

color_dict = {
    "Light Default" :    ("#000000" , "#ffffff") ,
    "Light Plus"    :    ("#474747" , "#e0e0e0") ,
    "Dark"          :    ("#c4c4c4" , "#2d2d2d") ,
    "Monokai"       :    ("#2d2d2d" , "#ffe8e8") ,
    "Night Blue"    :    ("#d3b774" , "#474747") ,
    "Light Red"     :    ("#ededed" , "#6b9dc2") ,
}


about = tk.Menu(main_menu,tearoff=False)





# *********************************** Toolbar **********************************

# FONT FAMILY
tool_bar1 = ttk.Label(naziya)
tool_bar1.pack(side=tk.TOP ,fill = tk.X)
tool_bar1.configure(background = "#ffffff")

font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar1 ,width = 30 , textvariable=font_family ,state = "readonly")
font_box ["values"] = font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0,column=0 ,padx=8 , pady=4)


# FONT SIZE
font_size = tk.IntVar()
font_size1 = ttk.Combobox(tool_bar1 ,width=10 ,textvariable= font_size ,state = "readonly")
font_size1["values"] = tuple(range(2,73))
font_size1.current(9)
font_size1.grid(row=0,column=1,padx=2)



os.chdir(r"D:\apk\exe\icons")
size = (15,15)
image_list = ("bold.png" ,"italic.png","underline.png","font_color.png","align_left.png","align_center.png","align_right.png")
for i in image_list:
    img = Image.open(os.path.join(os.getcwd(),i))
    img.thumbnail(size)
    level = os.path.join(os.getcwd(),i)
    img.save(level)
    
# BOLD BUTTON
bold_button = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\bold.png")
bold_button1 = tk.Button(tool_bar1 ,image= bold_button ,borderwidth = 0)
bold_button1.config(height=16,width=16,bg="#ffffff")
bold_button1.grid(row=0,column=2,padx=3)

# ITALIC BUTTON
italic_button = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\italic.png")
italic_button1 = tk.Button(tool_bar1 ,image= italic_button ,borderwidth = 0)
italic_button1.config(height=16,width=16,bg="#ffffff")
italic_button1.grid(row=0,column=3,padx=3)

# UNDERLINE BUTTON
underline_button = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\underline.png")
underline_button1 = tk.Button(tool_bar1 ,image= underline_button ,borderwidth = 0)
underline_button1.config(height=16,width=16,bg="#ffffff")
underline_button1.grid(row=0,column=4,padx=3)

# COLOR FONT BUTTON
color_font_button = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\font_color.png")
color_font_button1 = tk.Button(tool_bar1 ,image= color_font_button ,borderwidth = 0)
color_font_button1.config(height=16,width=16,bg="#ffffff")
color_font_button1.grid(row=0,column=5,padx=3)

# LEFT ALIGN BUTTON
leftalign_button = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\align_left.png")
leftalign_button1 = tk.Button(tool_bar1 ,image= leftalign_button ,borderwidth = 0)
leftalign_button1.config(height=16,width=16 ,bg="#ffffff")
leftalign_button1.grid(row=0,column=6,padx=3)

# CENTER ALIGN BUTTON
centeralign_button = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\align_center.png")
centeralign_button1 = tk.Button(tool_bar1 ,image= centeralign_button ,borderwidth = 0)
centeralign_button1.config(height=16,width=16,bg="#ffffff")
centeralign_button1.grid(row=0,column=7,padx=3)

# RIGHT ALIGN BUTTON
rightalign_button = tk.PhotoImage(file = r"D:\Apk\Exe\Icons\align_right.png")
rightalign_button1 = tk.Button(tool_bar1 ,image= rightalign_button ,borderwidth = 0)
rightalign_button1.config(height=16,width=16,bg="#ffffff")
rightalign_button1.grid(row=0,column=8,padx=3)







# **************************************** TEXT EDITOR ********************************************

text_editor = tk.Text(naziya)
text_editor.config(wrap="word" ,relief=tk.FLAT)

scroll_bar = tk.Scrollbar(naziya)
text_editor.focus()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH ,expand=True)
scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# Font Size And Family Functionality
current_font_family = "Arial"
current_text_size = 11

def NAZIYA(naziya):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family,current_text_size))

font_box.bind("<<ComboboxSelected>>" ,NAZIYA)

def NAZIYAPARVEEN(naziya):
    global current_text_size
    current_text_size = font_size.get()
    text_editor.configure(font=(current_font_family,current_text_size))

font_box.bind("<<ComboboxSelected>>" ,NAZIYA)
font_size1.bind("<<ComboboxSelected>>" ,NAZIYAPARVEEN)
 
text_editor.configure(font=("Arial" ,11))



# BOLD FUNCTION 

def bold_function():
    text_property = tk.font.Font(font = text_editor["font"])
    if text_property.actual()["weight"] == "normal":
        text_editor.configure(font=(current_font_family,current_text_size ,"bold"))

    else:
        text_editor.configure(font=(current_font_family,current_text_size ,"normal"))

bold_button1.configure(command = bold_function) 


# ITALIC FUNCTION

def italic_function():
    text_property = tk.font.Font(font = text_editor["font"])
    if text_property.actual()["slant"] == "roman":
        text_editor.configure(font=(current_font_family,current_text_size, "italic"))

    else:
        text_editor.configure(font=(current_font_family,current_text_size, "roman"))

italic_button1.configure(command = italic_function) 


# UNDERLINE FUNCTION

def underline_function():
    text_property = tk.font.Font(font = text_editor["font"])
    if text_property.actual()["underline"] == 0:
        text_editor.configure(font=(current_font_family,current_text_size ,"underline"))

    else:
        text_editor.configure(font=(current_font_family,current_text_size ,"normal"))

underline_button1.configure(command = underline_function) 


# COLOR CHANGE FUNCTION

def color_change():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
 
color_font_button1.configure(command = color_change)



# ALIGN LEFT FUNCTION

def align_left():
    text_content = text_editor.get(1.0, "end")
    text_editor.tag_config("left",justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT,text_content,"left")

leftalign_button1.configure(command=align_left)



# ALIGN RIGHT FUNCTION

def align_right():
    text_content = text_editor.get(1.0, "end")
    text_editor.tag_config("right",justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT,text_content,"right")

rightalign_button1.configure(command=align_right)



# ALIGN CENTER FUNCTION

def align_center():
    text_content = text_editor.get(1.0, "end")
    text_editor.tag_config("center",justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT,text_content,"center")

centeralign_button1.configure(command=align_center)









# ******************************* BOTTOM STATUS BAR ********************************

status_bar_bottom = tk.Label(naziya,text = "Status Bar")
status_bar_bottom.pack(side=tk.BOTTOM,fill=tk.X)

text_change = False
def counts(event=None):
    global text_change
    if text_editor.edit_modified():
        text_change = True
        words = len(text_editor.get(1.0 ,"end-1c").split())
        character = len(text_editor.get(1.0 , "end-1c"))
        status_bar_bottom.config(text=f"Character = {character}  Words = {words}")
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>" ,counts)





                                        # COMMANDS

# NEW FILE FUNCTION
url = ""
def new_file_function(event = None):
    global url
    url = ""
    text_editor.delete(1.0 ,tk.END)


# OPEN FUNCTION
def open_file_function(event =None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select File",filetypes=(("Text File" , "*.txt") , ("All Files" ,"*.*")))
    try:
        with open(url,"r") as np:
            text_editor.delete(1.0 ,tk.END)
            text_editor.insert(1.0 ,np.read())
    except FileNotFoundError:
        return
    except:
        return


# SAVE FUNCTION
def save_file_function(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url, "w" ,encoding="utf-8") as npw:
                npw.write(content)
                
        else:
            url = filedialog.asksaveasfile(mode = "w", defaultextension = ".txt" ,filetypes=(("Text File" , "*.txt") , ("All Files" ,"*.*")))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return



# SAVE AS FUNCTION
def save_as_function(event=None):
    global url
    try:
        content = text_editor.get(1.0,tk.END)
        url = filedialog.asksaveasfile(mode = "w", defaultextension = ".txt" ,filetypes=(("Text File" , "*.txt") , ("All Files" ,"*.*")))
        url.write(content) 
        url.close()
    except:
        return



def exit_function(event=None):
    global url, text_change
    try:
        if text_change:
            mbox = messagebox.askyesnocancel("Warning" , "Do You Want To Save This File ?")
            if mbox is True:
                if url:
                    content = text_editor.get(1.0 ,tk.END)
                    with open(url, "w" , encoding="utf-8") as wf:
                        wf.write(content)
                        naziya.destroy()
                
                else:
                    content2 = str(text_editor.get(1.0 ,tk.END))
                    url = filedialog.asksaveasfile(mode = "w", defaultextension = ".txt" ,filetypes=(("Text File" , "*.txt") , ("All Files" ,"*.*")))
                    url.write(content2)
                    url.close
                    naziya.destroy()

            elif mbox is False:
                naziya.destroy()
        else:
            naziya.destroy()
            
    except:
        return



# FILE COMMANDS
file.add_command(label = "New" , image=new_icon, compound = tk.LEFT ,accelerator= "Ctrl+N",command=new_file_function)
file.add_command(label = "Open" , image=open_icon, compound = tk.LEFT ,accelerator= "Ctrl+O", command=open_file_function)
file.add_separator()
file.add_command(label = "Save" , image=save_icon, compound = tk.LEFT ,accelerator= "Ctrl+S",command = save_file_function)
file.add_command(label = "Save As" , image=save_as_icon, compound = tk.LEFT ,accelerator= "Ctrl+Shift+S" ,command=save_as_function)
file.add_separator()
file.add_command(label = "Exit" , image=exit_icon, compound = tk.LEFT ,accelerator= "Ctrl+Q",command=exit_function)

 

# FIND FUNCTION
def find_function(event=None):

    def find_f():
        word = find_box.get()
        text_editor.tag_remove("match" , "1.0" ,tk.END)
        matches = 0
        if word:
            start_pos = "1.0"
            while True:
                start_pos = text_editor.search(word ,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match" ,start_pos ,end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config("match" ,foreground="white" , background="red")


    def replace_f():
        word = find_box.get()
        replace_text = replace_box.get()
        content = text_editor.get(1.0 ,tk.END)
        new_content = content.replace(word , replace_text)
        text_editor.delete(1.0 ,tk.END)
        text_editor.insert(1.0 , new_content)
        


    find_dialogue = tk.Toplevel()
    find_dialogue.geometry("450x250+500+200")
    find_dialogue.title("Find/Replace")
    find_dialogue.focus()
    find_dialogue.resizable(False,False)

    # Frame
    find_frame = ttk.LabelFrame(find_dialogue)
    find_frame.pack(pady=50,padx=60)

    # Label
    find_label = ttk.Label(find_frame ,text = "Find : ")
    replace_label = ttk.Label(find_frame ,text = "Replace : ")
    find_label.grid(row=0,column=0,padx=4,pady=4)
    replace_label.grid(row=1,column=0,padx=4,pady=4)

    # Entry Box
    find_box = ttk.Entry(find_frame ,width = 30)
    replace_box = ttk.Entry(find_frame ,width = 30) 
    find_box.grid(row=0,column=1,padx=4,pady=4)  
    replace_box.grid(row=1,column=1,padx=4,pady=4)
    
    # Button
    find_button = ttk.Button(find_frame, text = "Find" ,command = find_f)
    find_button.focus()
    replace_button = ttk.Button(find_frame, text = "Replace" ,command = replace_f)
    find_button.grid(row=2,column=0,padx=8,pady=4)  
    replace_button.grid(row=2,column=1,padx=8,pady=4)


    
    find_dialogue.mainloop()
    




# EDIT COMMANDS
edit.add_command(label = "Cut" , image = cut_icon ,compound= tk.LEFT ,accelerator= "Ctrl+X",command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label = "Copy" , image = copy_icon ,compound= tk.LEFT ,accelerator= "Ctrl+C",command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label = "Paste" , image = paste_icon ,compound= tk.LEFT ,accelerator= "Ctrl+V",command=lambda:text_editor.event_generate("<Control v>"))
edit.add_separator()
edit.add_command(label = "Clear" , image = clear_all_icon ,compound= tk.LEFT ,accelerator= "Ctrl+Alt+X",command=lambda:text_editor.delet(1.0, tk.END))
edit.add_command(label = "Find" , image = find_icon ,compound= tk.LEFT ,accelerator= "Ctrl+F",command=find_function)

# VIEW COMMANDS
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar1.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar_bottom.pack_forget()
        tool_bar1.pack(side = tk.TOP, fill =tk.X)
        text_editor.pack(fill = tk.BOTH,expand=True)
        status_bar_bottom.pack(side = tk.BOTTOM)
        show_toolbar = True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar_bottom.pack_forget()
        show_statusbar = False
    else:
        status_bar_bottom.pack(side =tk.BOTTOM)
        show_statusbar = True


view.add_checkbutton(label= "Tool Bar" , onvalue = True , offvalue = False ,variable= show_toolbar, image = tool_bar, compound = tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label= "Status Bar" , onvalue = True , offvalue = False ,variable= show_statusbar,image = status_bar, compound = tk.LEFT, command=hide_statusbar)


# COLOR THEME COMMANDS
count = 0
sec = 0
for i in color_dict:
    colortheme.add_radiobutton(label = i, image = color_icon[count], variable=theme_choice, compound = tk.LEFT  ,command = functiontuple[sec])
    count += 1
    sec += 1

# ABOUT COMMAND
about.add_command(label = "Help", command=help_function)
about.add_command(label = "About" ,command=about_function)







                                    # CASCADE

# CASCADE
main_menu.add_cascade(label = "File" , menu = file)   #FILE
main_menu.add_cascade(label = "Edit" , menu = edit)   #EDIT
main_menu.add_cascade(label = "View" , menu = view)   #VIEW
main_menu.add_cascade(label = "Color Theme" , menu = colortheme)    #COLOR THEME
main_menu.add_cascade(label = "About" , menu = about)  #ABOUT


# ENDING
naziya.config(menu= main_menu)

# SHORTCUT KEY BINDING
naziya.bind("<Control-n>" , new_file_function)
naziya.bind("<Control-o>" , open_file_function)
naziya.bind("<Control-s>" , save_file_function)
naziya.bind("<Control-Shift-S>" , save_as_function)
naziya.bind("<Control-q>" , exit_function)
naziya.bind("<Control-f>" , find_function)

naziya.mainloop()