#Import necessary modules
from tkinter import *

#Create a contact form/ tracing form class
class TracingForm():
    #Saving User's Information Label
    def user_information(self):
      self.user_information_window = Tk()
      self.user_information_window.title("Personal Data")
      self.user_information_window.geometry("1000x400")

      self.name()
      self.age()

      self.user_information_window.mainloop()
    #Get name
    def name(self):
      first_name = Label(self.user_information_window, text="First Name: ")
      first_name.grid(row=0, column=0, padx=5, pady=10)
      entry_first_name = Entry(self.user_information_window)
      entry_first_name.grid(row=0, column=1)

      second_name = Label(self.user_information_window, text="Second Name: ")
      second_name.grid(row=0, column=2, padx=5, pady=10)
      entry_second_name = Entry(self.user_information_window)
      entry_second_name.grid(row=0, column=3)

      last_name = Label(self.user_information_window, text="Last Name: ")
      last_name.grid(row=0, column=4, padx=5, pady=10)
      entry_last_name = Entry(self.user_information_window)
      entry_last_name.grid(row=0, column=5)
      
    
    #Get age 
    def age(self):
       age = Label(self.user_information_window, text="Age (yrs. old):")
       age.grid(row=1, column=0, padx=5, pady=10)
       entry_age = Entry(self.user_information_window)
       entry_age.grid(row=1, column=1)
        




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