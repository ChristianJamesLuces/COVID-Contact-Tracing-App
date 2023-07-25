
#Import necessary modules
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv


#Create a contact form/ tracing form class
class TracingForm():
    def user_information(self):
        self.user_information_window = tk.Tk()
        self.user_information_window.title("Personal Data")
        self.user_information_window.geometry("1250x650")
        self.user_information_window.config(bg="#ECDADD")
        self.user_information_window.resizable(False,False)

        #Get name
        self.first_name = tk.Label(self.user_information_window, text="First Name: ", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.first_name.grid(row=0, column=0, padx=5, pady=10)
        self.entry_first_name = tk.Entry(self.user_information_window)
        self.entry_first_name.grid(row=0, column=1)
        
        self.second_name = tk.Label(self.user_information_window, text="Second Name: ", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.second_name.grid(row=0, column=2, padx=5, pady=10)
        self.entry_second_name = tk.Entry(self.user_information_window)
        self.entry_second_name.grid(row=0, column=3)
        
        self.last_name = tk.Label(self.user_information_window, text="Last Name: ", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.last_name.grid(row=0, column=4, padx=5, pady=10)
        self.entry_last_name = tk.Entry(self.user_information_window)
        self.entry_last_name.grid(row=0, column=5)
    
        #Get age 
        self.age_label = tk.Label(self.user_information_window, text="Age (yrs. old):", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.age_label.grid(row=1, column=0, padx=5, pady=10)
        self.entry_age = tk.Entry(self.user_information_window)
        self.entry_age.grid(row=1, column=1)
    
        #Get sex
        self.sex_label = tk.Label(self.user_information_window, text="Sex:", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.sex_label.grid(row=2, column=0, padx=5, pady=10)
        
        self.sex_box = ttk.Combobox(self.user_information_window, values= ["Male", "Female", "Intersex"], width=8)
        self.sex_box.grid(row=2, column=1, padx=5, pady=10)
    
        #Get adress
        self.address_label = tk.Label(self.user_information_window, text="Address:", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.address_label.grid(row=3, column=0, padx=5, pady=10)
        
        self.house_number_street_village = tk.Label(self.user_information_window, text="House No./Street/Village:", bg="#ECDADD")
        self.house_number_street_village.grid(row=3, column=1, padx=5, pady=10)
        self.entry_house_number_street_village = tk.Entry(self.user_information_window)
        self.entry_house_number_street_village.grid(row=3, column=2)
        
        self.barangay = tk.Label(self.user_information_window, text="Barangay:", bg="#ECDADD")
        self.barangay.grid(row=3, column=3, padx=5, pady=10)
        self.entry_barangay = tk.Entry(self.user_information_window)
        self.entry_barangay.grid(row=3, column=4)
        
        self.city = tk.Label(self.user_information_window, text="City/Town:", bg="#ECDADD")
        self.city.grid(row=3, column=5, padx=5, pady=10)
        self.entry_city = tk.Entry(self.user_information_window)
        self.entry_city.grid(row=3, column=6)

        #Get contact number
        self.contact_number_label = tk.Label(self.user_information_window, text="Contact No. (ex.09...):", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.contact_number_label.grid(row=4, column=0, padx=5, pady=10)
        self.entry_contact_number = tk.Entry(self.user_information_window)
        self.entry_contact_number.grid(row=4, column=1)

        #Get email adress
        self.email_label = tk.Label(self.user_information_window, text="Email Address:", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.email_label.grid(row=5, column=0, padx=5, pady=10)
        self.entry_email = tk.Entry(self.user_information_window)
        self.entry_email.grid(row=5, column=1)
    
        #Get last location
        self.location_label = tk.Label(self.user_information_window, text="Last Visited Place:", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.location_label.grid(row=6, column=0, padx=5, pady=10)
        
        self.last_house_number_street_village = tk.Label(self.user_information_window, text="House No./Street/Village:", bg="#ECDADD")
        self.last_house_number_street_village.grid(row=6, column=1, padx=5, pady=10)
        self.entry_last_house_number_street_village = tk.Entry(self.user_information_window)
        self.entry_last_house_number_street_village.grid(row=6, column=2)
        
        self.last_barangay = tk.Label(self.user_information_window, text="Barangay:", bg="#ECDADD")
        self.last_barangay.grid(row=6, column=3, padx=5, pady=10)
        self.entry_last_barangay = tk.Entry(self.user_information_window)
        self.entry_last_barangay.grid(row=6, column=4)
        
        self.last_city = tk.Label(self.user_information_window, text="City/Town:", bg="#ECDADD")
        self.last_city.grid(row=6, column=5, padx=5, pady=10)
        self.entry_last_city = tk.Entry(self.user_information_window)
        self.entry_last_city.grid(row=6, column=6)

        #Get date for that last place visited
        self.date_label = tk.Label(self.user_information_window, text="Date of visit:", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.date_label.grid(row=7, column=0, padx=5, pady=10)
        
        self.month = tk.Label(self.user_information_window, text="Month:", bg="#ECDADD")
        self.month.grid(row=7, column=1, padx=5, pady=10)
        self.entry_month = tk.Spinbox(self.user_information_window, from_=0, to=12)
        self.entry_month.grid(row=7, column=2, padx=5, pady=10)
        
        self.day = tk.Label(self.user_information_window, text="Day:", bg="#ECDADD")
        self.day.grid(row=7, column=3, padx=5, pady=10)
        self.entry_day = tk.Spinbox(self.user_information_window, from_=0, to=31)
        self.entry_day.grid(row=7, column=4, padx=5, pady=10)
        
        self.year = tk.Label(self.user_information_window, text="Year:", bg="#ECDADD")
        self.year.grid(row=7, column=5, padx=5, pady=10)
        self.entry_year= tk.Spinbox(self.user_information_window, from_=2019, to=2023)
        self.entry_year.grid(row=7, column=6, padx=5, pady=10)
    
        #Get vaccine status
        self.vaccine_status_label = tk.Label(self.user_information_window, text="COVID-19 Vaccination Status:", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.vaccine_status_label.grid(row=8, column=0, padx=5, pady=10)

        self.vaccine_box = ttk.Combobox(self.user_information_window, values= ["Not Yet", "1st Dose", "2nd Dose", "1st Booster Shot", "2nd Booster Shot"])
        self.vaccine_box.grid(row=8, column=1, padx=5, pady=10)
    
        #Get COVID-19 test result
        self.covid_result_label = tk.Label(self.user_information_window, text="COVID-19 Test Result:", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.covid_result_label.grid(row=9, column=0, padx=5, pady=10)

        self.covid_box = ttk.Combobox(self.user_information_window, values=["No", "Yes-Positive", "Yes-Negative", "Yes-Pending"])
        self.covid_box.grid(row=9, column=1, padx=5, pady=10)
    
        #Get if the user has close contact
        self.close_contact_label = tk.Label(self.user_information_window, text="Exposed to COVID-19 in the last 14 days?", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.close_contact_label.grid(row=10, column=0, padx=5, pady=10)

        self.close_contact_box = ttk.Combobox(self.user_information_window, values=["No", "Yes"])
        self.close_contact_box.grid(row=10, column=1, padx=5, pady=10)

        #Get symptoms
        self.symptoms_label = tk.Label(self.user_information_window, text="Experiencing symptoms in the past 7 days?", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.symptoms_label.grid(row=11, column=0, padx=5, pady=10)
        
        self.symptoms_label = tk.Label(self.user_information_window, text="Symptoms: fever, cough, or other flu like symptoms", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.symptoms_label.grid(row=11, column=1, padx=5, pady=10)

        self.symptoms_box = ttk.Combobox(self.user_information_window, values=["No", "Yes"])
        self.symptoms_box.grid(row=11, column=2, padx=5, pady=10)
        
        #Get name of emergency contact
        self.emergency_name_label = tk.Label(self.user_information_window, text="Emergency Contact's Name: ", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.emergency_name_label.grid(row=13, column=0, padx=5, pady=10)
        self.entry_emergency_name = tk.Entry(self.user_information_window)
        self.entry_emergency_name.grid(row=13, column=1)
        self.contact_name = tk.Label(self.user_information_window, text="(First Name/Second Name/Last Name)", bg="#ECDADD")
        self.contact_name.grid(row=13, column=2, padx=5, pady=10)
    
        #Get contact number of emergency contact
        self.emergency_number_label = tk.Label(self.user_information_window, text="Emergency Contact Phone Number (09...): ", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.emergency_number_label.grid(row=14, column=0, padx=5, pady=10)
        self.entry_emergency_number = tk.Entry(self.user_information_window)
        self.entry_emergency_number.grid(row=14, column=1)

        #Get email address of emergency contact
        self.emergency_email_label = tk.Label(self.user_information_window, text="Emergency Contact Email Address: ", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.emergency_email_label.grid(row=15, column=0, padx=5, pady=10)
        self.entry_emergency_email = tk.Entry(self.user_information_window)
        self.entry_emergency_email.grid(row=15, column=1)

    
        self.submit_button = tk.Button(self.user_information_window, text="Submit", fg="green", font=("Time", 11, "bold"), command=self.submit_contacts)
        self.submit_button.place(x=1150, y=600)

    #Saving the user's data
    def submit_contacts(self):
        first_name = self.entry_first_name.get().lower()
        second_name = self.entry_second_name.get().lower()
        last_name =  self.entry_last_name.get().lower()
        age = self.entry_age.get()
        sex = self.sex_box.get().lower()
        address = {
            "House_No_Street_Village": self.entry_house_number_street_village.get().lower(),
            "Barangay": self.entry_barangay.get().lower(),
            "City/Town": self.entry_city.get().lower(),
        }
        contact_number = self.entry_contact_number.get()
        email = self.entry_email.get()
        visited_recently = {
            "House_No_Street_Village": self.entry_last_house_number_street_village.get().lower(),
            "Barangay": self.entry_last_barangay.get().lower(),
            "City": self.entry_last_city.get().lower(),
        }
        date_of_visit= {"Date": f"{self.entry_month.get()}/{self.entry_day.get()}/{self.entry_year.get()}"}
        vaccine_status = self.vaccine_box.get().lower()
        test_result = self.covid_box.get().lower()
        close_contact = self.close_contact_box.get().lower()
        symptoms_value = self.symptoms_box.get().lower()

        emergency_name =  self.entry_emergency_name.get().lower()
        emergency_number =  self.entry_emergency_number.get()
        emergency_email = self.entry_emergency_email.get()

         # Prepare data for writing to CSV
        user_data = [
            first_name,
            second_name,
            last_name,
            age,
            sex,
            f"{address['House_No_Street_Village']}, {address['Barangay']}, {address['City/Town']}",
            contact_number,
            email,
            f"{visited_recently['House_No_Street_Village']}, {visited_recently['Barangay']}, {visited_recently['City']}",
            date_of_visit,
            vaccine_status,
            test_result,
            close_contact,
            symptoms_value,
            emergency_name,
            emergency_number,
            emergency_email,

        ]

        # Write data to contact_list.csv
        with open('contact_list.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(user_data)

        # Close the user_information_window after submitting
        self.user_information_window.quit()

        # Show a message box to inform the user that their data has been saved
        messagebox.showinfo("Data Saved", "Your contact information has been successfully saved.")
