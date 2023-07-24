import tkinter as tk
from tkinter import ttk

class TracingForm():
    def user_information(self):
        self.user_information_window = tk.Tk()
        self.user_information_window.title("Personal Data")
        self.user_information_window.geometry("1250x650")
        self.user_information_window.config(bg="#ECDADD")
        self.user_information_window.resizable(False,False)

        self.name()
        self.age()
        self.sex()
        self.address()
        self.contact_number()
        self.email_adress()
        self.last_place()
        self.last_date()
        self.vaccine_status()
        self.test_result()
        self.close_contact()
        self.symptoms()
        self.emergency_name()

    #Get name
    def name(self):
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
    def age(self):
        self.age_label = tk.Label(self.user_information_window, text="Age (yrs. old):", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.age_label.grid(row=1, column=0, padx=5, pady=10)
        self.entry_age = tk.Entry(self.user_information_window)
        self.entry_age.grid(row=1, column=1)
    
    #Get sex
    def sex(self):
        self.sex_label = tk.Label(self.user_information_window, text="Sex:", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.sex_label.grid(row=2, column=0, padx=5, pady=10)
        
        self.sex_box = ttk.Combobox(self.user_information_window, values= ["Male", "Female", "Intersex"], width=8)
        self.sex_box.grid(row=2, column=1, padx=5, pady=10)
    
    #Get adress
    def address(self):
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
    def contact_number(self):
        self.contact_number_label = tk.Label(self.user_information_window, text="Contact No. (ex.09...):", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.contact_number_label.grid(row=4, column=0, padx=5, pady=10)
        self.entry_contact_number = tk.Entry(self.user_information_window)
        self.entry_contact_number.grid(row=4, column=1)

    #Get email adress
    def email_adress(self):
        self.email_label = tk.Label(self.user_information_window, text="Email Address:", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.email_label.grid(row=5, column=0, padx=5, pady=10)
        self.entry_email = tk.Entry(self.user_information_window)
        self.entry_email.grid(row=5, column=1)
    
    #Get last location
    def last_place(self):
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
    def last_date(self):
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
    def vaccine_status(self):
        self.vaccine_status_label = tk.Label(self.user_information_window, text="COVID-19 Vaccination Status:", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.vaccine_status_label.grid(row=8, column=0, padx=5, pady=10)

        self.vaccine_box = ttk.Combobox(self.user_information_window, values= ["Not Yet", "1st Dose", "2nd Dose", "1st Booster Shot", "2nd Booster Shot"])
        self.vaccine_box.grid(row=8, column=1, padx=5, pady=10)
    
    #Get COVID-19 test result
    def test_result(self):
        self.covid_result_label = tk.Label(self.user_information_window, text="COVID-19 Test Result:", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.covid_result_label.grid(row=9, column=0, padx=5, pady=10)

        self.covid_box = ttk.Combobox(self.user_information_window, values=["No", "Yes-Positive", "Yes-Negative", "Yes-Pending"])
        self.covid_box.grid(row=9, column=1, padx=5, pady=10)
    
    #Get if the user has close contact
    def close_contact(self):
        self.close_contact_label = tk.Label(self.user_information_window, text="Exposed to COVID-19 in the last 14 days?", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.close_contact_label.grid(row=10, column=0, padx=5, pady=10)

        self.close_contact_box = ttk.Combobox(self.user_information_window, values=["No", "Yes"])
        self.close_contact_box.grid(row=10, column=1, padx=5, pady=10)

    #Get symptoms
    def symptoms(self):
        self.symptoms_label = tk.Label(self.user_information_window, text="Experiencing symptoms in the past 7 days?", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.symptoms_label.grid(row=11, column=0, padx=5, pady=10)
        
        self.fever_check = tk.StringVar()
        self.fever = tk.Checkbutton(self.user_information_window, text="Fever", variable=self.fever_check, onvalue="Yes", offvalue="No", bg="#ECDADD")
        self.fever.grid(row=11, column=1)
        
        self.cough_check = tk.StringVar()
        self.cough = tk.Checkbutton(self.user_information_window, text="Cough", variable=self.cough_check, onvalue="Yes", offvalue="No", bg="#ECDADD")
        self.cough.grid(row=11, column=2)
        
        self.muscle_check = tk.StringVar()
        self.muscle_body_pains = tk.Checkbutton(self.user_information_window, text="Muscle/body pains", variable=self.muscle_check, onvalue="Yes", offvalue="No", bg="#ECDADD")
        self.muscle_body_pains.grid(row=11, column=3)
        
        self.sore_check = tk.StringVar()
        self.sore_throat = tk.Checkbutton(self.user_information_window, text="Soar throat", variable=self.sore_check, onvalue="Yes", offvalue="No", bg="#ECDADD")
        self.sore_throat.grid(row=11, column=4)
        
        self.diarrhea_check = tk.StringVar()
        self.diarrhea = tk.Checkbutton(self.user_information_window, text="Diarrhea", variable=self.diarrhea_check, onvalue="Yes", offvalue="No", bg="#ECDADD")
        self.diarrhea.grid(row=11, column=5)
        
        self.headache_check = tk.StringVar()
        self.headache = tk.Checkbutton(self.user_information_window, text="Headache", variable=self.headache_check, onvalue="Yes", offvalue="No", bg="#ECDADD")
        self.headache.grid(row=11, column=6)
        
        self.shortness_breath_check = tk.StringVar()
        self.shortness_of_breath = tk.Checkbutton(self.user_information_window, text="Shortness of breath", variable=self.shortness_breath_check, onvalue="Yes", offvalue="No", bg="#ECDADD")
        self.shortness_of_breath.grid(row=12, column=1)
        
        self.difficulty_breath_check = tk.StringVar()
        self.difficulty_of_breathing = tk.Checkbutton(self.user_information_window, text="Difficulty of breathing", variable=self.difficulty_breath_check, onvalue="Yes", offvalue="No", bg="#ECDADD")
        self.difficulty_of_breathing.grid(row=12, column=2)
        
        self.taste_check = tk.StringVar()
        self.loss_of_taste = tk.Checkbutton(self.user_information_window, text="Loss of taste", variable=self.taste_check, onvalue="Yes", offvalue="No", bg="#ECDADD")
        self.loss_of_taste.grid(row=12, column=3)
        
        self.smell_check = tk.StringVar()
        self.loss_of_smell = tk.Checkbutton(self.user_information_window, text="Loss of smell", variable=self.smell_check, onvalue="Yes", offvalue="No", bg="#ECDADD")
        self.loss_of_smell.grid(row=12, column=4)
        
        self.none_check = tk.StringVar()
        self.none_of_the_above = tk.Checkbutton(self.user_information_window, text="None of the above", variable=self.none_check, onvalue="Yes", offvalue="No", bg="#ECDADD")
        self.none_of_the_above.grid(row=12, column=5)
    
    #Get name of emergency contact
    def emergency_name(self):
        self.emergency_name_label = tk.Label(self.user_information_window, text="Emergency Contact's Name: ", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.emergency_name_label.grid(row=13, column=0, padx=5, pady=10)
        self.entry_emergency_name = tk.Entry(self.user_information_window)
        self.entry_emergency_name.grid(row=13, column=1)
        self.contact_name = tk.Label(self.user_information_window, text="(First Name/Second Name/Last Name)", bg="#ECDADD")
        self.contact_name.grid(row=13, column=2, padx=5, pady=10)



        