#Import necessary modules
from tkinter import *

#Create a contact form/ tracing form class
class TracingForm():
    #Saving User's Information Label
    def user_information(self):
      self.user_information_window = Tk()
      self.user_information_window.title("Personal Data")
      self.user_information_window.geometry("1000x400")
      
      #Get name
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
      age = Label(self.user_information_window, text="Age (yrs. old):")
      age.grid(row=1, column=0, padx=5, pady=10)
      entry_age = Entry(self.user_information_window)
      entry_age.grid(row=1, column=1)
      
      #Get sex
      sex = Label(self.user_information_window, text="Sex:")
      sex.grid(row=2, column=0, padx=5, pady=10)
      
      radio = IntVar(None)
      male_sex = Radiobutton(self.user_information_window,variable=radio, text="male", value=1)
      male_sex.grid(row=2, column=1)
      
      female_sex = Radiobutton(self.user_information_window, variable=radio, text="female", value=2)
      female_sex.grid(row=2, column=2)
      
      inter_sex = Radiobutton(self.user_information_window, variable=radio, text="intersex", value=3)
      inter_sex.grid(row=2, column=3)
      
      #Get address
      address = Label(self.user_information_window, text="Address:")
      address.grid(row=3, column=0, padx=5, pady=10)
      
      house_number_street_village = Label(self.user_information_window, text="House No./Street/Village:")
      house_number_street_village.grid(row=3, column=1, padx=5, pady=10)
      house_number_street_village = Entry(self.user_information_window)
      house_number_street_village.grid(row=3, column=2)
      
      barangay = Label(self.user_information_window, text="Barangay:")
      barangay.grid(row=3, column=3, padx=5, pady=10)
      barangay = Entry(self.user_information_window)
      barangay.grid(row=3, column=4)
      
      city = Label(self.user_information_window, text="City:")
      city.grid(row=3, column=5, padx=5, pady=10)
      city = Entry(self.user_information_window)
      city.grid(row=3, column=6)
      
      #Get contact number
      contact_number = Label(self.user_information_window, text="Contact No. (ex.09...):")
      contact_number.grid(row=4, column=0, padx=5, pady=10)
      contact_number = Entry(self.user_information_window)
      contact_number.grid(row=4, column=1)
      
      self.user_information_window.mainloop()
    
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