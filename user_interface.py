#Christian James M. Luces | BSCpE 1-5 | Final Project - COVID Contact Tracing App

#Import necessary modules
from edit_file import FileHandler
from tracing_form import TracingForm
from PIL import Image, ImageTk
import tkinter as tk


#Create class
class UserInterface:
    #Show introduction
    def introduction(self):
        self.window = tk.Tk()
        self.window.title("Introduction - CoviCompanion")
        self.window.geometry("800x400")

        with open("introduction.txt", "r") as file:
            introduction_text = file.read()

            introduction_label = tk.Label(self.window, text=introduction_text, fg="black", font=("Arial", 12))
            introduction_label.pack()

            proceed_button = tk.Button(self.window, text="Proceed to Main Window", command=self.main_window)
            proceed_button.pack()

        self.window.mainloop()
    
    #Create a main window
    def main_window(self):
        self.window.destroy()

        main_window = tk.Tk()
        main_window.title("Covid Tracing App")
        main_window.geometry("1100x400")
        main_window.config(bg="#2F0909")
        main_window.resizable(False,False)

        
        image = Image.open("background.png")
        resize_image = image.resize((800, 400), Image.ANTIALIAS)

        background = ImageTk.PhotoImage(resize_image)
        image_background = tk.Label(main_window, image= background, bg="white", borderwidth=0)
        image_background.place(x=300, y=0)

        

        label = tk.Label(main_window, text = "Welcome to CoviCompanion", fg="white", font=("Arial", 15, "bold"))
        label.place(x=20, y=20)

        self.contact_form(main_window)
        self.search_data(main_window)

        main_window.mainloop()

    #Create a Contact Form button
    def contact_form(self, main_window):
        tracing_form = TracingForm()
        contact_button = tk.Button(main_window, text="Contact Form", fg="blue", command=lambda: tracing_form.user_information(), font=("Times New Roman", 14) )
        contact_button.place(x=80, y=120)

    def search_data(self, main_window):
        file_handler = FileHandler()
        finder_button = tk.Button(main_window, text="Search Contact", fg="blue", command=lambda: file_handler.search_window(), font=("Times New Roman", 14) )
        finder_button.place(x=80, y=180)