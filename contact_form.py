#Import necessary modules
from tkinter import *

#Create a contact form/ tracing form class
class TracingForm():
    #Saving User's Information Label
    def user_information(self):
      self.user_information_window = Tk()
      self.user_information_window.title("Personal Data")
      self.user_information_window.geometry("1250x600")
      
      #Get name
      first_name = Label(self.user_information_window, text="First Name: ", font=("Arial", 9, "bold"))
      first_name.grid(row=0, column=0, padx=5, pady=10)
      entry_first_name = Entry(self.user_information_window)
      entry_first_name.grid(row=0, column=1)

      second_name = Label(self.user_information_window, text="Second Name: ", font=("Arial", 9, "bold"))
      second_name.grid(row=0, column=2, padx=5, pady=10)
      entry_second_name = Entry(self.user_information_window)
      entry_second_name.grid(row=0, column=3)

      last_name = Label(self.user_information_window, text="Last Name: ", font=("Arial", 9, "bold"))
      last_name.grid(row=0, column=4, padx=5, pady=10)
      entry_last_name = Entry(self.user_information_window)
      entry_last_name.grid(row=0, column=5)
      
      #Get age 
      age = Label(self.user_information_window, text="Age (yrs. old):", font=("Arial", 9, "bold"))
      age.grid(row=1, column=0, padx=5, pady=10)
      entry_age = Entry(self.user_information_window)
      entry_age.grid(row=1, column=1)
      
      #Get sex
      sex = Label(self.user_information_window, text="Sex:", font=("Arial", 9, "bold"))
      sex.grid(row=2, column=0, padx=5, pady=10)
      
      radio = IntVar()
      male_sex = Radiobutton(self.user_information_window,variable=radio, text="male", value=1)
      male_sex.grid(row=2, column=1)
      
      
      female_sex = Radiobutton(self.user_information_window, variable=radio, text="female", value=2)
      female_sex.grid(row=2, column=2)
      
      
      inter_sex = Radiobutton(self.user_information_window, variable=radio, text="intersex", value=3)
      inter_sex.grid(row=2, column=3)
      
      #Get address
      address = Label(self.user_information_window, text="Address:", font=("Arial", 9, "bold"))
      address.grid(row=3, column=0, padx=5, pady=10)
      
      house_number_street_village = Label(self.user_information_window, text="House No./Street/Village:")
      house_number_street_village.grid(row=3, column=1, padx=5, pady=10)
      entry_house_number_street_village = Entry(self.user_information_window)
      entry_house_number_street_village.grid(row=3, column=2)
      
      barangay = Label(self.user_information_window, text="Barangay:")
      barangay.grid(row=3, column=3, padx=5, pady=10)
      entry_barangay = Entry(self.user_information_window)
      entry_barangay.grid(row=3, column=4)
      
      city = Label(self.user_information_window, text="City/Town:")
      city.grid(row=3, column=5, padx=5, pady=10)
      entry_city = Entry(self.user_information_window)
      entry_city.grid(row=3, column=6)
      
      #Get contact number
      contact_number = Label(self.user_information_window, text="Contact No. (ex.09...):", font=("Arial", 9, "bold"))
      contact_number.grid(row=4, column=0, padx=5, pady=10)
      entry_contact_number = Entry(self.user_information_window)
      entry_contact_number.grid(row=4, column=1)
      
      #Get email address
      email = Label(self.user_information_window, text="Email Address:", font=("Arial", 9, "bold"))
      email.grid(row=5, column=0, padx=5, pady=10)
      entry_email = Entry(self.user_information_window)
      entry_email.grid(row=5, column=1)

      #Get Last Location
      location = Label(self.user_information_window, text="Last Visited Place:", font=("Arial", 9, "bold"))
      location.grid(row=6, column=0, padx=5, pady=10)

      last_house_number_street_village = Label(self.user_information_window, text="House No./Street/Village:")
      last_house_number_street_village.grid(row=6, column=1, padx=5, pady=10)
      entry_last_house_number_street_village = Entry(self.user_information_window)
      entry_last_house_number_street_village.grid(row=6, column=2)

      last_barangay = Label(self.user_information_window, text="Barangay:")
      last_barangay.grid(row=6, column=3, padx=5, pady=10)
      entry_last_barangay = Entry(self.user_information_window)
      entry_last_barangay.grid(row=6, column=4)

      last_city = Label(self.user_information_window, text="City/Town:")
      last_city.grid(row=6, column=5, padx=5, pady=10)
      entry_last_city = Entry(self.user_information_window)
      entry_last_city.grid(row=6, column=6)

      #Get date for that location
      date = Label(self.user_information_window, text="Date of visit:", font=("Arial", 9, "bold"))
      date.grid(row=7, column=0, padx=5, pady=10)

      month = Label(self.user_information_window, text="Month:")
      month.grid(row=7, column=1, padx=5, pady=10)
      entry_month = Spinbox(self.user_information_window, from_=0, to=12)
      entry_month.grid(row=7, column=2, padx=5, pady=10)

      day = Label(self.user_information_window, text="Day:")
      day.grid(row=7, column=3, padx=5, pady=10)
      entry_day = Spinbox(self.user_information_window, from_=0, to=31)
      entry_day.grid(row=7, column=4, padx=5, pady=10)

      year = Label(self.user_information_window, text="Year:")
      year.grid(row=7, column=5, padx=5, pady=10)
      entry_year= Spinbox(self.user_information_window, from_=2019, to=2023)
      entry_year.grid(row=7, column=6, padx=5, pady=10)

      #Get vaccine status
      vaccine_status = Label(self.user_information_window, text="COVID-19 Vaccination Status:", font=("Arial", 9, "bold"))
      vaccine_status.grid(row=8, column=0, padx=5, pady=10)
      
      radio = IntVar()
      not_yet = Radiobutton(self.user_information_window,variable=radio, text="Not Yet", value=1)
      not_yet.grid(row=8, column=1)
      
      
      first_dose = Radiobutton(self.user_information_window, variable=radio, text="1st Dose", value=2)
      first_dose.grid(row=8, column=2)
      
      
      second_dose = Radiobutton(self.user_information_window, variable=radio, text="2nd Dose", value=3)
      second_dose.grid(row=8, column=3)

      
      first_booster_shot = Radiobutton(self.user_information_window, variable=radio, text="1st Booster Shot", value=4)
      first_booster_shot.grid(row=8, column=4)

      
      second_booster_shot = Radiobutton(self.user_information_window, variable=radio, text="2nd Booster Shot", value=5)
      second_booster_shot.grid(row=8, column=5)

      #Get COVID test result


      self.user_information_window.mainloop()

      
#Get name of guardian
#Get contact number of guardian
#Get email address of guardian

#Get symptoms
