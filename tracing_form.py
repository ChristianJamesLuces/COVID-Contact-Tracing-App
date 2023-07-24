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