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

    
    def name(self):
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
    
    def age(self):
        #Get age 
        self.age_label = tk.Label(self.user_information_window, text="Age (yrs. old):", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.age_label.grid(row=1, column=0, padx=5, pady=10)
        self.entry_age = tk.Entry(self.user_information_window)
        self.entry_age.grid(row=1, column=1)
    
    def sex(self):
        self.sex_label = tk.Label(self.user_information_window, text="Sex:", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.sex_label.grid(row=2, column=0, padx=5, pady=10)
        
        self.sex_box = ttk.Combobox(self.user_information_window, values= ["Male", "Female", "Intersex"], width=8)
        self.sex_box.grid(row=2, column=1, padx=5, pady=10)
    
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

    def contact_number(self):
        self.contact_number_label = tk.Label(self.user_information_window, text="Contact No. (ex.09...):", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.contact_number_label.grid(row=4, column=0, padx=5, pady=10)
        self.entry_contact_number = tk.Entry(self.user_information_window)
        self.entry_contact_number.grid(row=4, column=1)