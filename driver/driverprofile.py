from tkinter import *
from PIL import ImageTk, Image
import customtkinter
from libs import Global


class DriverProfile():
    def __init__(self, main):
        self.main = main
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')
        self.main.title("{} Profile".format(Global.currentDriver[1]))
        self.main.iconbitmap("C:\\Users\KIIT\OneDrive\Documents\cme project\Cab-Booking-System\Images\logo.ico")
        width = 750
        height = 350
        self.main.resizable(0,0)
        myscreenwidth = self.main.winfo_screenwidth()
        myscreenheight = self.main.winfo_screenheight()
        xCordinate = int((myscreenwidth / 2) - (width / 2))
        yCordinate = int((myscreenheight / 2) - (height / 2))
        self.main.geometry('{}x{}+{}+{}'.format(width, height, xCordinate+50, yCordinate - 50))
        self.main.maxsize(950, 400)


        font720 =customtkinter.CTkFont(family='Times New Roman', size=19, weight='normal')


        centerFrame = customtkinter.CTkFrame(master=self.main, width=710, height=250)
        centerFrame.place(x=20, y=60)


        namelbl = customtkinter.CTkLabel(centerFrame, text="Name: ", font=font720)
        namelbl.place(x=50, y=100)


        namelbl1=customtkinter.CTkLabel(centerFrame, text="{}".format(Global.currentDriver[1]), font=font720)
        namelbl1.place(x=150, y=100)



        mobile = customtkinter.CTkLabel(centerFrame, text="Mobile: ", font=font720)
        mobile.place(x=50, y=150)


        mobile1 = customtkinter.CTkLabel(centerFrame, text="{}".format(Global.currentDriver[2]), font=font720)
        mobile1.place(x=150, y=150)


        email = customtkinter.CTkLabel(centerFrame, text="Email: ", font=font720)
        email.place(x=410, y=100)


        email1 = customtkinter.CTkLabel(centerFrame, text="{}".format(Global.currentDriver[3]), font=font720)
        email1.place(x=510, y=100)


        license = customtkinter.CTkLabel(centerFrame, text="License No: ", font=font720)
        license.place(x=410, y=150)


        license1 = customtkinter.CTkLabel(centerFrame, text="{}".format(Global.currentDriver[4]), font=font720)
        license1.place(x=510, y=150)



        user_image = ImageTk.PhotoImage(Image.open("C:\\Users\KIIT\OneDrive\Documents\cme "
                                                   "project\Cab-Booking-System\Images\\user-solid-120.png"))
        user_image_label = Label(self.main, image=user_image, bg="#212325")
        user_image_label.image = user_image
        user_image_label.place(x=400, y=20)


if __name__=='__main__':
    main=customtkinter.CTk()
    DriverProfile(main)
    main.mainloop()