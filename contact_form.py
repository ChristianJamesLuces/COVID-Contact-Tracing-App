#Import necessary modules
from tkinter import *
from tkinter import messagebox

#Create a contact form/ tracing form class
class TracingForm():
    #Saving User's Information Label
    def user_information(self):
        self.user_information_window = Tk()
        self.user_information_window.title("Personal Data")
        self.user_information_window.geometry("1250x650")
        self.user_information_window.config(bg="#ECDADD")
        self.user_information_window.resizable(False,False)
        
        #Get name
        self.first_name = Label(self.user_information_window, text="First Name: ", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.first_name.grid(row=0, column=0, padx=5, pady=10)
        self.entry_first_name = Entry(self.user_information_window)
        self.entry_first_name.grid(row=0, column=1)
        
        self.second_name = Label(self.user_information_window, text="Second Name: ", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.second_name.grid(row=0, column=2, padx=5, pady=10)
        self.entry_second_name = Entry(self.user_information_window)
        self.entry_second_name.grid(row=0, column=3)
        
        self.last_name = Label(self.user_information_window, text="Last Name: ", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.last_name.grid(row=0, column=4, padx=5, pady=10)
        self.entry_last_name = Entry(self.user_information_window)
        self.entry_last_name.grid(row=0, column=5)
        
        #Get age 
        self.age = Label(self.user_information_window, text="Age (yrs. old):", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.age.grid(row=1, column=0, padx=5, pady=10)
        self.entry_age = Entry(self.user_information_window)
        self.entry_age.grid(row=1, column=1)
        
        #Get sex
        self.sex = Label(self.user_information_window, text="Sex:", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.sex.grid(row=2, column=0, padx=5, pady=10)
        
        self.sex_radio = StringVar()
        self.male_sex = Radiobutton(self.user_information_window,variable=self.sex_radio, text="male", value=1, bg="#ECDADD")
        self.male_sex.grid(row=2, column=1)
        
        self.female_sex = Radiobutton(self.user_information_window, variable=self.sex_radio, text="female", value=2, bg="#ECDADD")
        self.female_sex.grid(row=2, column=2)
        
        self.inter_sex = Radiobutton(self.user_information_window, variable=self.sex_radio, text="intersex", value=3, bg="#ECDADD")
        self.inter_sex.grid(row=2, column=3)
        
        #Get address
        self.address = Label(self.user_information_window, text="Address:", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.address.grid(row=3, column=0, padx=5, pady=10)
        
        self.house_number_street_village = Label(self.user_information_window, text="House No./Street/Village:", bg="#ECDADD")
        self.house_number_street_village.grid(row=3, column=1, padx=5, pady=10)
        self.entry_house_number_street_village = Entry(self.user_information_window)
        self.entry_house_number_street_village.grid(row=3, column=2)
        
        self.barangay = Label(self.user_information_window, text="Barangay:", bg="#ECDADD")
        self.barangay.grid(row=3, column=3, padx=5, pady=10)
        self.entry_barangay = Entry(self.user_information_window)
        self.entry_barangay.grid(row=3, column=4)
        
        self.city = Label(self.user_information_window, text="City/Town:", bg="#ECDADD")
        self.city.grid(row=3, column=5, padx=5, pady=10)
        self.entry_city = Entry(self.user_information_window)
        self.entry_city.grid(row=3, column=6)
        
        #Get contact number
        self.contact_number = Label(self.user_information_window, text="Contact No. (ex.09...):", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.contact_number.grid(row=4, column=0, padx=5, pady=10)
        self.entry_contact_number = Entry(self.user_information_window)
        self.entry_contact_number.grid(row=4, column=1)
        
        #Get email address
        self.email = Label(self.user_information_window, text="Email Address:", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.email.grid(row=5, column=0, padx=5, pady=10)
        self.entry_email = Entry(self.user_information_window)
        self.entry_email.grid(row=5, column=1)
        
        #Get Last Location
        self.location = Label(self.user_information_window, text="Last Visited Place:", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.location.grid(row=6, column=0, padx=5, pady=10)
        
        self.last_house_number_street_village = Label(self.user_information_window, text="House No./Street/Village:", bg="#ECDADD")
        self.last_house_number_street_village.grid(row=6, column=1, padx=5, pady=10)
        self.entry_last_house_number_street_village = Entry(self.user_information_window)
        self.entry_last_house_number_street_village.grid(row=6, column=2)
        
        self.last_barangay = Label(self.user_information_window, text="Barangay:", bg="#ECDADD")
        self.last_barangay.grid(row=6, column=3, padx=5, pady=10)
        self.entry_last_barangay = Entry(self.user_information_window)
        self.entry_last_barangay.grid(row=6, column=4)
        
        self.last_city = Label(self.user_information_window, text="City/Town:", bg="#ECDADD")
        self.last_city.grid(row=6, column=5, padx=5, pady=10)
        self.entry_last_city = Entry(self.user_information_window)
        self.entry_last_city.grid(row=6, column=6)
        
        #Get date for that location
        self.date = Label(self.user_information_window, text="Date of visit:", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.date.grid(row=7, column=0, padx=5, pady=10)
        
        self.month = Label(self.user_information_window, text="Month:", bg="#ECDADD")
        self.month.grid(row=7, column=1, padx=5, pady=10)
        self.entry_month = Spinbox(self.user_information_window, from_=0, to=12)
        self.entry_month.grid(row=7, column=2, padx=5, pady=10)
        
        self.day = Label(self.user_information_window, text="Day:", bg="#ECDADD")
        self.day.grid(row=7, column=3, padx=5, pady=10)
        self.entry_day = Spinbox(self.user_information_window, from_=0, to=31)
        self.entry_day.grid(row=7, column=4, padx=5, pady=10)
        
        self.year = Label(self.user_information_window, text="Year:", bg="#ECDADD")
        self.year.grid(row=7, column=5, padx=5, pady=10)
        self.entry_year= Spinbox(self.user_information_window, from_=2019, to=2023)
        self.entry_year.grid(row=7, column=6, padx=5, pady=10)
        
        #Get vaccine status
        self.vaccine_status = Label(self.user_information_window, text="COVID-19 Vaccination Status:", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.vaccine_status.grid(row=8, column=0, padx=5, pady=10)
        
        self.vaccine_radio = StringVar()
        self.not_yet = Radiobutton(self.user_information_window,variable=self.vaccine_radio, text="Not Yet", value=1, bg="#ECDADD")
        self.not_yet.grid(row=8, column=1)
        
        self.first_dose = Radiobutton(self.user_information_window, variable=self.vaccine_radio, text="1st Dose", value=2, bg="#ECDADD")
        self.first_dose.grid(row=8, column=2)
        
        self.second_dose = Radiobutton(self.user_information_window, variable=self.vaccine_radio, text="2nd Dose", value=3, bg="#ECDADD")
        self.second_dose.grid(row=8, column=3)
        
        self.first_booster_shot = Radiobutton(self.user_information_window, variable=self.vaccine_radio, text="1st Booster Shot", value=4, bg="#ECDADD")
        self.first_booster_shot.grid(row=8, column=4)
        
        self.second_booster_shot = Radiobutton(self.user_information_window, variable=self.vaccine_radio, text="2nd Booster Shot", value=5, bg="#ECDADD")
        self.second_booster_shot.grid(row=8, column=5)
        
        #Get COVID test result
        self.covid_result = Label(self.user_information_window, text="COVID-19 Test Result:", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.covid_result.grid(row=9, column=0, padx=5, pady=10)
        
        self.test_radio = StringVar()
        self.no_result = Radiobutton(self.user_information_window,variable=self.test_radio, text="No", value=1, bg="#ECDADD")
        self.no_result.grid(row=9, column=1)
        
        self.yes_positive = Radiobutton(self.user_information_window, variable=self.test_radio, text="Yes-Positive", value=2, bg="#ECDADD")
        self.yes_positive.grid(row=9, column=2)
        
        self.yes_negative = Radiobutton(self.user_information_window, variable=self.test_radio, text="Yes-Negative", value=3, bg="#ECDADD")
        self.yes_negative.grid(row=9, column=3)
        
        self.yes_pending = Radiobutton(self.user_information_window, variable=self.test_radio, text="Yes-Pending", value=4, bg="#ECDADD")
        self.yes_pending.grid(row=9, column=4)
        
        #Get if the user has close contact
        self.close_contact = Label(self.user_information_window, text="Exposed to COVID-19 in the last 14 days?", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.close_contact.grid(row=10, column=0, padx=5, pady=10)
        
        self.close_radio = StringVar()
        self.no = Radiobutton(self.user_information_window,variable=self.close_radio, text="No", value="No", bg="#ECDADD")
        self.no.grid(row=10, column=1)
        
        self.yes = Radiobutton(self.user_information_window, variable=self.close_radio, text="Yes", value="Yes", bg="#ECDADD")
        self.yes.grid(row=10, column=2)
        
        #Get symptoms
        self.symptoms = Label(self.user_information_window, text="Experiencing symptoms in the past 7 days?", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.symptoms.grid(row=11, column=0, padx=5, pady=10)
        
        self.fever_check = StringVar(value="No")
        self.fever = Checkbutton(self.user_information_window, text="Fever", variable=self.fever_check, onvalue="Yes", offvalue="No", bg="#ECDADD")
        self.fever.grid(row=11, column=1)
        
        self.cough_check = StringVar(value="No")
        self.cough = Checkbutton(self.user_information_window, text="Cough", variable=self.cough_check, onvalue="Yes", offvalue="No", bg="#ECDADD")
        self.cough.grid(row=11, column=2)
        
        self.muscle_check = StringVar(value="No")
        self.muscle_body_pains = Checkbutton(self.user_information_window, text="Muscle/body pains", variable=self.muscle_check, onvalue="Yes", offvalue="No", bg="#ECDADD")
        self.muscle_body_pains.grid(row=11, column=3)
        
        self.sore_check = StringVar(value="No")
        self.sore_throat = Checkbutton(self.user_information_window, text="Soar throat", variable=self.sore_check, onvalue="Yes", offvalue="No", bg="#ECDADD")
        self.sore_throat.grid(row=11, column=4)
        
        self.diarrhea_check = StringVar(value="No")
        self.diarrhea = Checkbutton(self.user_information_window, text="Diarrhea", variable=self.diarrhea_check, onvalue="Yes", offvalue="No", bg="#ECDADD")
        self.diarrhea.grid(row=11, column=5)
        
        self.headache_check = StringVar(value="No")
        self.headache = Checkbutton(self.user_information_window, text="Headache", variable=self.headache_check, onvalue="Yes", offvalue="No", bg="#ECDADD")
        self.headache.grid(row=11, column=6)
        
        self.shortness_breath_check = StringVar(value="No")
        self.shortness_of_breath = Checkbutton(self.user_information_window, text="Shortness of breath", variable=self.shortness_breath_check, onvalue="Yes", offvalue="No", bg="#ECDADD")
        self.shortness_of_breath.grid(row=12, column=1)
        
        self.difficulty_breath_check = StringVar(value="No")
        self.difficulty_of_breathing = Checkbutton(self.user_information_window, text="Difficulty of breathing", variable=self.difficulty_breath_check, onvalue="Yes", offvalue="No", bg="#ECDADD")
        self.difficulty_of_breathing.grid(row=12, column=2)
        
        self.taste_check = StringVar(value="No")
        self.loss_of_taste = Checkbutton(self.user_information_window, text="Loss of taste", variable=self.taste_check, onvalue="Yes", offvalue="No", bg="#ECDADD")
        self.loss_of_taste.grid(row=12, column=3)
        
        self.smell_check = StringVar(value="No")
        self.loss_of_smell = Checkbutton(self.user_information_window, text="Loss of smell", variable=self.smell_check, onvalue="Yes", offvalue="No", bg="#ECDADD")
        self.loss_of_smell.grid(row=12, column=4)
        
        self.none_check = StringVar(value="No")
        self.none_of_the_above = Checkbutton(self.user_information_window, text="None of the above", variable=self.none_check, onvalue="Yes", offvalue="No", bg="#ECDADD")
        self.none_of_the_above.grid(row=12, column=5)
        
        
        #Get name of emergency contact
        self.emergency_name = Label(self.user_information_window, text="Emergency Contact's Name: ", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.emergency_name.grid(row=13, column=0, padx=5, pady=10)
        self.entry_emergency_name = Entry(self.user_information_window)
        self.entry_emergency_name.grid(row=13, column=1)
        self.contact_name = Label(self.user_information_window, text="(First Name/Second Name/Last Name)", bg="#ECDADD")
        self.contact_name.grid(row=13, column=2, padx=5, pady=10)
        
        #Get contact number of emergency contact
        self.emergency_number = Label(self.user_information_window, text="Emergency Contact Phone Number: ", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.emergency_number.grid(row=14, column=0, padx=5, pady=10)
        self.entry_emergency_number = Entry(self.user_information_window)
        self.entry_emergency_number.grid(row=14, column=1)
        
        #Get email address of emergency contact
        self.emergency_email = Label(self.user_information_window, text="Emergency Contact Email Address: ", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.emergency_email.grid(row=15, column=0, padx=5, pady=10)
        self.entry_emergency_email = Entry(self.user_information_window)
        self.entry_emergency_email.grid(row=15, column=1)

        #Creat a submit button
        submit_button = Button(self.user_information_window, text="Submit", command=self.save_contact, fg="green", font=("Time", 11, "bold"))
        submit_button.place(x=1150, y=600)

        self.user_information_window.mainloop()

    #Save the contact
    def save_contact(self):
        first_name = self.entry_first_name.get()
        second_name = self.entry_second_name.get()
        last_name = self.entry_last_name.get()
        age = self.entry_age.get()
        sex = self.sex_radio.get()
        address = {
            "House_No_Street_Village": self.entry_house_number_street_village.get(),
            "Barangay": self.entry_barangay.get(),
            "City/Town": self.entry_city.get(),
            }
        contact_number = self.entry_contact_number.get()
        email = self.entry_email.get()
        last_location = {
            "House_No_Street_Village": self.entry_last_house_number_street_village.get(),
            "Barangay": self.entry_last_barangay.get(),
            "City": self.entry_last_city.get(),
            "Date": f"{self.entry_month.get()}/{self.entry_day.get()}/{self.entry_year.get()}",
            }
        vaccine_status = self.vaccine_radio.get()
        covid_result = self.test_radio.get()
        close_contact = self.close_radio.get()
       
        symptoms_value = {
            "Fever": self.fever_check.get(),
            "Cough": self.cough_check.get(),
            "Muscle/body pains": self.muscle_check.get(),
            "Soar throat": self.sore_check.get(),
            "Diarrhea": self.diarrhea_check.get(),
            "Headache": self.headache_check.get(),
            "Shortness of breath": self.shortness_breath_check.get(),
            "Difficulty of breathing": self.difficulty_breath_check.get(),
            "Loss of taste": self.taste_check.get(),
            "Loss of smell": self.smell_check.get(),
            "None of the above": self.none_check.get(),
        }
        

        emergency_contact = {
            "Name": self.entry_emergency_name.get(),
            "Phone_Number": self.entry_emergency_number.get(),
            "Email": self.entry_emergency_email.get(),
            }

        #Check if all fields are filled
        required_fields = [first_name, second_name, last_name, age, sex,
                       address["House_No_Street_Village"], address["Barangay"], address["City/Town"],
                       contact_number, email,
                       last_location["House_No_Street_Village"], last_location["Barangay"],
                       last_location["City"], last_location["Date"],
                       vaccine_status, covid_result, close_contact]
        
        if all(field.strip() != "" for field in required_fields):
            contact_data = {
            "First_Name": first_name,
            "Second_Name": second_name,
            "Last_Name": last_name,
            "Age": age,
            "Sex": sex,
            "Address": address,
            "Contact_Number": contact_number,
            "Email": email,
            "Last_Location": last_location,
            "Vaccine_Status": vaccine_status,
            "COVID_Result": covid_result,
            "Close_Contact": close_contact,
            "Symptoms": symptoms_value,
            "Emergency_Contact": emergency_contact
            }

            #Save the contact data to the a file
            with open("user_database.txt", "a") as file:
                user_info = ",".join(contact_data.values())
                file.write(user_info + "\n")
            
            #Display a message if it's a successfull submission
            messagebox.showinfo("Success", "Contact data submitted successfully!")
            self.user_information_window.destroy()
        
        else:
            #Display a message if there is missing information
            messagebox.showwarning("Incomplete Information", "Please fill in all the fields before submitting.")

      


    

