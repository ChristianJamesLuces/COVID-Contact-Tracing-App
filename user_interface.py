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
        self.window.geometry("800x170")

        with open("introduction.txt", "r") as file:
            introduction_text = file.read()

            introduction_label = tk.Label(self.window, text=introduction_text, fg="black", font=("Arial", 12, ))
            introduction_label.pack()

            proceed_button = tk.Button(self.window, text="Proceed to Main Window", command=self.main_window, fg="#2F0909", font=("Arial", 12, "bold"))
            proceed_button.place(x=575, y=130)

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

        

        label = tk.Label(main_window, text = "Welcome to CoviCompanion", fg="white",bg="#2F0909", font=("Arial", 15, "bold"))
        label.place(x=20, y=20)

        self.contact_form(main_window)
        self.search_data(main_window)

        main_window.mainloop()

    #Create a Contact Form button
    def contact_form(self, main_window):
        tracing_form = TracingForm()
        contact_image = Image.open("contact_form.png")
        resize_image = contact_image.resize((110, 50), Image.ANTIALIAS)

        contact_image_button = ImageTk.PhotoImage(resize_image)
        contact_button = tk.Button(main_window, image=contact_image_button, command=lambda: tracing_form.user_information(), borderwidth=1 )
        contact_button.image = contact_image_button
        contact_button.place(x=80, y=120)

    def search_data(self, main_window):
        file_handler = FileHandler()
        search_image = Image.open("search_contact.png")
        resize_image = search_image.resize((110, 50), Image.ANTIALIAS)

        search_image_button = ImageTk.PhotoImage(resize_image)
        finder_button = tk.Button(main_window, image=search_image_button, command=lambda: file_handler.search_window(), borderwidth=0)
        finder_button.image = search_image_button
        finder_button.place(x=80, y=230)