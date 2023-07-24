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
      covid_result = Label(self.user_information_window, text="COVID-19 Test Result:", font=("Arial", 9, "bold"))
      covid_result.grid(row=9, column=0, padx=5, pady=10)

      radio = IntVar()
      no_result = Radiobutton(self.user_information_window,variable=radio, text="No", value=1)
      no_result.grid(row=9, column=1)
      
      
      yes_positive = Radiobutton(self.user_information_window, variable=radio, text="Yes-Positive", value=2)
      yes_positive.grid(row=9, column=2)
      
      
      yes_negative = Radiobutton(self.user_information_window, variable=radio, text="Yes-Negative", value=3)
      yes_negative.grid(row=9, column=3)

      
      yes_pending = Radiobutton(self.user_information_window, variable=radio, text="Yes-Pending", value=4)
      yes_pending.grid(row=9, column=4)

      #Get if the user has close contact
      close_contact = Label(self.user_information_window, text="Exposed to COVID-19 in the last 14 days?", font=("Arial", 9, "bold"))
      close_contact.grid(row=10, column=0, padx=5, pady=10)

      radio = IntVar()
      no = Radiobutton(self.user_information_window,variable=radio, text="No", value=1)
      no.grid(row=10, column=1)
      
      
      yes = Radiobutton(self.user_information_window, variable=radio, text="Yes", value=2)
      yes.grid(row=10, column=2)

      #Get symptoms
      symptoms = Label(self.user_information_window, text="Experiencing symptoms in the past 7 days?", font=("Arial", 9, "bold"))
      symptoms.grid(row=11, column=0, padx=5, pady=10)

      fever = Checkbutton(self.user_information_window, text="Fever")
      fever.grid(row=11, column=1)

      cough = Checkbutton(self.user_information_window, text="Cough")
      cough.grid(row=11, column=2)

      muscle_body_pains = Checkbutton(self.user_information_window, text="Muscle/body pains")
      muscle_body_pains.grid(row=11, column=3)
      
      sore_throat = Checkbutton(self.user_information_window, text="Sore throat")
      sore_throat.grid(row=11, column=4)

      diarrhea = Checkbutton(self.user_information_window, text="Diarrhea")
      diarrhea.grid(row=11, column=5)

      headache = Checkbutton(self.user_information_window, text="Headache")
      headache.grid(row=11, column=6)

      shortness_of_breath = Checkbutton(self.user_information_window, text="Shortness of breath")
      shortness_of_breath.grid(row=12, column=1)

      difficulty_of_breathing = Checkbutton(self.user_information_window, text="Difficulty of breathing")
      difficulty_of_breathing.grid(row=12, column=2)

      loss_of_taste = Checkbutton(self.user_information_window, text="Loss of taste")
      loss_of_taste.grid(row=12, column=3)

      loss_of_smell = Checkbutton(self.user_information_window, text="Loss of smell")
      loss_of_smell.grid(row=12, column=4)

      none_of_the_above = Checkbutton(self.user_information_window, text="None of the above")
      none_of_the_above.grid(row=12, column=5)


      #Get name of emergency contact
      emergency_name = Label(self.user_information_window, text="Emergency Contact's Name: ", font=("Arial", 9, "bold"))
      emergency_name.grid(row=13, column=0, padx=5, pady=10)
      entry_emergency_name = Entry(self.user_information_window)
      entry_emergency_name.grid(row=13, column=1)
      contact_name = Label(self.user_information_window, text="(First Name/Second Name/Last Name)")
      contact_name.grid(row=13, column=2, padx=5, pady=10)

      #Get contact number of emergency contact
      emergency_number = Label(self.user_information_window, text="Emergency Contact Phone Number: ", font=("Arial", 9, "bold"))
      emergency_number.grid(row=14, column=0, padx=5, pady=10)
      entry_emergency_number = Entry(self.user_information_window)
      entry_emergency_number.grid(row=14, column=1)


      self.user_information_window.mainloop()

      

#Get contact number of emergency contact
#Get email address of emergency contact
