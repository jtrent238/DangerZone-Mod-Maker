import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("DangerZone ModMaker | by jtrent238")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_28=tk.Label(root)
        ft = tkFont.Font(family='Times',size=30)
        GLabel_28["font"] = ft
        GLabel_28["fg"] = "#333333"
        GLabel_28["justify"] = "center"
        GLabel_28["text"] = "DangerZone Mod Maker"
        GLabel_28.place(x=0,y=20,width=407,height=30)

        GLineEdit_47=tk.Entry(root)
        GLineEdit_47["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_47["font"] = ft
        GLineEdit_47["fg"] = "#333333"
        GLineEdit_47["justify"] = "center"
        GLineEdit_47["text"] = "My Awesome Mod"
        GLineEdit_47.place(x=110,y=70,width=150,height=25)

        GLabel_766=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_766["font"] = ft
        GLabel_766["fg"] = "#333333"
        GLabel_766["justify"] = "center"
        GLabel_766["text"] = "Mod Name: "
        GLabel_766.place(x=30,y=70,width=70,height=25)

        GLabel_457=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_457["font"] = ft
        GLabel_457["fg"] = "#333333"
        GLabel_457["justify"] = "center"
        GLabel_457["text"] = "Main Class: "
        GLabel_457.place(x=30,y=110,width=70,height=25)

        GLineEdit_26=tk.Entry(root)
        GLineEdit_26["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_26["font"] = ft
        GLineEdit_26["fg"] = "#333333"
        GLineEdit_26["justify"] = "center"
        GLineEdit_26["text"] = "MyAwesomeModMain"
        GLineEdit_26.place(x=110,y=110,width=150,height=25)

        GLabel_471=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_471["font"] = ft
        GLabel_471["fg"] = "#333333"
        GLabel_471["justify"] = "center"
        GLabel_471["text"] = "Mod Author: "
        GLabel_471.place(x=30,y=150,width=76,height=30)

        GLineEdit_8=tk.Entry(root)
        GLineEdit_8["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_8["font"] = ft
        GLineEdit_8["fg"] = "#333333"
        GLineEdit_8["justify"] = "center"
        GLineEdit_8["text"] = "awesomesauce74"
        GLineEdit_8.place(x=110,y=150,width=150,height=25)

        GLabel_126=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_126["font"] = ft
        GLabel_126["fg"] = "#333333"
        GLabel_126["justify"] = "center"
        GLabel_126["text"] = "Mod Version: "
        GLabel_126.place(x=270,y=70,width=92,height=30)

        GLineEdit_596=tk.Entry(root)
        GLineEdit_596["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_596["font"] = ft
        GLineEdit_596["fg"] = "#333333"
        GLineEdit_596["justify"] = "center"
        GLineEdit_596["text"] = "1.0.0.0"
        GLineEdit_596.place(x=360,y=70,width=150,height=25)

        GLabel_397=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_397["font"] = ft
        GLabel_397["fg"] = "#333333"
        GLabel_397["justify"] = "center"
        GLabel_397["text"] = "DZ Version: "
        GLabel_397.place(x=280,y=110,width=70,height=25)

        CreateItemButton=tk.Button(root)
        CreateItemButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        CreateItemButton["font"] = ft
        CreateItemButton["fg"] = "#000000"
        CreateItemButton["justify"] = "center"
        CreateItemButton["text"] = "Create Item"
        CreateItemButton.place(x=30,y=340,width=85,height=25)
        CreateItemButton["command"] = self.CreateItemButton_command

        CreateBlockButton=tk.Button(root)
        CreateBlockButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        CreateBlockButton["font"] = ft
        CreateBlockButton["fg"] = "#000000"
        CreateBlockButton["justify"] = "center"
        CreateBlockButton["text"] = "Create Block"
        CreateBlockButton.place(x=120,y=340,width=85,height=25)
        CreateBlockButton["command"] = self.CreateBlockButton_command

        GLabel_364=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_364["font"] = ft
        GLabel_364["fg"] = "#333333"
        GLabel_364["justify"] = "center"
        GLabel_364["text"] = "Tool Box"
        GLabel_364.place(x=30,y=300,width=70,height=25)

        CompileButton=tk.Button(root)
        CompileButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        CompileButton["font"] = ft
        CompileButton["fg"] = "#000000"
        CompileButton["justify"] = "center"
        CompileButton["text"] = "Compile"
        CompileButton.place(x=520,y=460,width=70,height=25)
        CompileButton["command"] = self.CompileButton_command

        GLabel_100=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_100["font"] = ft
        GLabel_100["fg"] = "#333333"
        GLabel_100["justify"] = "center"
        GLabel_100["text"] = "Mod Information"
        GLabel_100.place(x=30,y=200,width=125,height=25)

        GLabel_688=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_688["font"] = ft
        GLabel_688["fg"] = "#333333"
        GLabel_688["justify"] = "center"
        GLabel_688["text"] = "Compiled FIlename: "
        GLabel_688.place(x=40,y=230,width=120,height=25)

        GLabel_695=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_695["font"] = ft
        GLabel_695["fg"] = "#333333"
        GLabel_695["justify"] = "center"
        GLabel_695["text"] = "{file_name}"
        GLabel_695.place(x=160,y=230,width=70,height=25)

        GLineEdit_755=tk.Entry(root)
        GLineEdit_755["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_755["font"] = ft
        GLineEdit_755["fg"] = "#333333"
        GLineEdit_755["justify"] = "center"
        GLineEdit_755["text"] = "2.1"
        GLineEdit_755.place(x=360,y=110,width=150,height=25)

        SaveButton=tk.Button(root)
        SaveButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        SaveButton["font"] = ft
        SaveButton["fg"] = "#000000"
        SaveButton["justify"] = "center"
        SaveButton["text"] = "Save"
        SaveButton.place(x=90,y=460,width=70,height=25)
        SaveButton["command"] = self.SaveButton_command

        LoadButton=tk.Button(root)
        LoadButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        LoadButton["font"] = ft
        LoadButton["fg"] = "#000000"
        LoadButton["justify"] = "center"
        LoadButton["text"] = "Load"
        LoadButton.place(x=10,y=460,width=70,height=25)
        LoadButton["command"] = self.LoadButton_command

    def CreateItemButton_command(self):
        print("command")


    def CreateBlockButton_command(self):
        print("command")


    def CompileButton_command(self):
        print("command")


    def SaveButton_command(self):
        print("command")


    def LoadButton_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
