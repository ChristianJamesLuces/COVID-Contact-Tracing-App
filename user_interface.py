#Christian James M. Luces | BSCpE 1-5 | Final Project - COVID Contact Tracing App

#Import necessary modules
from tkinter import *
from tracing_form import TracingForm
from file_operations import FileHandling



#Create class
class UserInterface:
    #Show introduction
    def introduction(self):
        self.window = Tk()
        self.window.title("Introduction - CoviCompanion")
        self.window.geometry("800x400")

        with open("introduction.txt", "r") as file:
            introduction_text = file.read()

            introduction_label = Label(self.window, text=introduction_text, fg="black", font=("Arial", 12))
            introduction_label.pack()

            proceed_button = Button(self.window, text="Proceed to Main Window", command=self.main_window)
            proceed_button.pack()

        self.window.mainloop()
    #Create a main window
    def main_window(self):
        self.window.destroy()

        main_window = Tk()
        main_window.title("Covid Tracing App")
        main_window.geometry("1250x400")
        

        label = Label(main_window, text = "Welcome to CoviCompanion", fg="black", font=("Arial", 15, "bold"))
        label.place(x=80, y=20)

        self.contact_form(main_window)
        self.search(main_window)

        main_window.mainloop()

    #Create a Contact Form button
    def contact_form(self, main_window):
        tracing_form = TracingForm()
        contact_button = Button(main_window, text="Contact Form", fg="blue", command=lambda: tracing_form.user_information(), font=("Times New Roman", 14) )
        contact_button.place(x=80, y=120)

    #Create a Search button
    def search(self, main_window):
        file_handler = FileHandling()
        search_button = Button(main_window, text="Search Contact", fg="blue", command=lambda: file_handler.search_window(), font=("Times New Roman", 14))
        search_button.place(x=80, y=200)
    




