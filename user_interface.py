#Christian James M. Luces | BSCpE 1-5 | Final Project - COVID Contact Tracing App

#Import necessary modules
from tkinter import *



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
        

        label = Label(self.window, text = "Welcome to CoviCompanion", fg="black", font=("Arial", 15, "bold"))
        label.place (x=80, y=20)

        main_window.mainloop()
    #Create a Contact Form button

      
    #Saving User's Information Label
    #Get name
#Get age
#Get sex
#Get address
#Get contact number
#Get email address

#Saving User's Emergency Information Label
#Get name of guardian
#Get contact number of guardian
#Get email address of guardian

#User's Health Declaration Label
#Get vaccine status
#Get symptoms
#Get COVID test result
#Get travel history

#Show introduction
#Ask for User's consent

app = UserInterface()
app.introduction()