#Christian James M. Luces | BSCpE 1-5 | Final Project - COVID Contact Tracing App

#Import necessary modules
from tkinter import *



#Create class
class UserInterface:
    def __init__(self):
        self.window = Tk()
        self.main_window()
        
        self.window.mainloop()
    #Create a main window
    def main_window(self):
        self.window.title("Covid Tracing App")
        self.window.geometry("1250x400")
        

        label = Label(self.window, text = "Welcome to COVID Contact Tracing App", fg="black", font=("Arial", 15, "bold"))
        label.place (x=780, y=20)


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

