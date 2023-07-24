
#Import necessary modules
import tkinter as tk
from tkinter import messagebox
from tracing_form import TracingForm
import csv


#Create file handling class
class FileHandling(TracingForm):
    #Saving the user's data
    def submit_contacts(self):
        first_name = self.entry_first_name.get()
        second_name = self.entry_second_name.get()
        last_name =  self.entry_last_name.get()
        age = self.entry_age.get()
        sex = self.sex_box.get
        address = {
            "House_No_Street_Village": self.entry_house_number_street_village.get(),
            "Barangay": self.entry_barangay.get(),
            "City/Town": self.entry_city.get(),
        }
        contact_number = self.entry_contact_number.get()
        email = self.entry_email.get()
        visited_recently = {
            "House_No_Street_Village": self.entry_last_house_number_street_village.get(),
            "Barangay": self.entry_last_barangay.get(),
            "City": self.entry_last_city.get(),
            "Date": f"{self.entry_month.get()}/{self.entry_day.get()}/{self.entry_year.get()}",
        }
        vaccine_status = self.vaccine_box.get()
        test_result = self.covid_box.get()
        close_contact = self.close_contact_box.get()
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

        emergency_name =  self.entry_emergency_name.get()
        emergency_number =  self.entry_emergency_number.get()
        emergency_email = self.entry_emergency_email.get()

        # Check if any required fields are empty
        required_fields = [first_name, last_name, age, sex, address["House_No_Street_Village"],
                           address["Barangay"], address["City/Town"], contact_number, email,
                           emergency_name, emergency_number, emergency_email]
        
        if any(not field for field in required_fields):
            messagebox.showerror("Error", "Please fill in all the required information.")
            return
        
        # Create a single line of data in CSV format
        contact_data = f"Name: {last_name}, {first_name}, {second_name} Gender: {sex} Age: {age} " \
                       f"Address: {address['House_No_Street_Village']}, {address['Barangay']}, {address['City/Town']} " \
                       f"Phone Number: {contact_number} Email: {email} " \
                       f"Contact Person: {emergency_name} Phone Number: {emergency_number} " \
                       f"Email: {emergency_email} " \
                       f"Vaccination Status: {vaccine_status} Symptoms: {', '.join(symptoms_value[key] for key in symptoms_value if symptoms_value[key])} " \
                       f"Exposed to a probable case: {close_contact} Has Contact (to a probable case): {test_result}"
        
        # Save data to a CSV file
        with open("contacts.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([contact_data])

        messagebox.showinfo("Success", "Contact information saved successfully.")
    
    #Search for the data
    #def search(self):





