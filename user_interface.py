#Christian James M. Luces | BSCpE 1-5 | Final Project - COVID Contact Tracing App

#Import necessary modules

from tracing_form import TracingForm
from PIL import ImageTk, Image
import csv
import tkinter as tk
from tkinter import scrolledtext



#Create class
class UserInterface:
    #Show introduction
    def introduction(self):
        self.window = tk.Tk()
        self.window.title("Introduction - CoviCompanion")
        self.window.geometry("800x400")

        with open("introduction.txt", "r") as file:
            introduction_text = file.read()

            introduction_label = tk.Label(self.window, text=introduction_text, fg="black", font=("Arial", 12))
            introduction_label.pack()

            proceed_button = tk.Button(self.window, text="Proceed to Main Window", command=self.main_window)
            proceed_button.pack()

        self.window.mainloop()
    
    #Create a main window
    def main_window(self):
        self.window.destroy()

        main_window = tk.Tk()
        main_window.title("Covid Tracing App")
        main_window.geometry("1250x400")
        

        label = tk.Label(main_window, text = "Welcome to CoviCompanion", fg="black", font=("Arial", 15, "bold"))
        label.place(x=80, y=20)

        self.contact_form(main_window)

        main_window.mainloop()

    #Create a Contact Form button
    def contact_form(self, main_window):
        tracing_form = TracingForm()
        contact_button = tk.Button(main_window, text="Contact Form", fg="blue", command=lambda: tracing_form.user_information(), font=("Times New Roman", 14) )
        contact_button.place(x=80, y=120)

        finder_button = tk.Button(main_window, text="Search Contact", fg="blue", command=self.search_window, font=("Times New Roman", 14) )
        finder_button.place(x=80, y=180)
    
    #Create a search window
    def search_window(self):
        search_window = tk.Tk()
        search_window.title("Search Contact - CoviCompanion")
        search_window.geometry("800x400")

        search_label = tk.Label(search_window, text="Enter the First Name to search:", font=("Arial", 12))
        search_label.pack()

        self.search_entry = tk.Entry(search_window, font=("Arial", 12))
        self.search_entry.pack()
        self.search_button(search_window)

    def search_button(self, search_window):
        search_button = tk.Button(search_window, text="Search", command=self.search_contact)
        search_button.pack()


        self.result_label = tk.Label(search_window, text="", font=("Arial", 12))
        self.result_label.pack()
    

    def search_contact(self):
        full_name = self.search_entry.get().strip().lower()

        if full_name == "":
            self.result_label.config(text="Please enter a name to search.")
            return

        found_data = []
        with open("contact_list.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                full_row_name = " ".join(row[:3]).lower()
                if full_name in full_row_name:
                    found_data.append(row)

        if found_data:
            self.show_search_results(found_data)
        else:
            self.result_label.config(text="No matching data found.")

     # Show the search results in a new window
    def show_search_results(self, data):
        result_window = tk.Toplevel()
        result_window.title("Search Results - CoviCompanion")
        result_window.geometry("800x400")

        result_label = tk.Label(result_window, text="Search Results:", font=("Arial", 15, "bold"))
        result_label.pack()

        # Create a scrolled text widget for displaying search results
        scroll_text = scrolledtext.ScrolledText(result_window, wrap=tk.WORD, width=100, height=20)
        scroll_text.pack()

        # Display the search results in the specified format
        for row in data:
            first_name, second_name, last_name, age, sex, address, contact_number, email, visited_recently, date_of_visit, vaccine_status,\
            test_result, close_contact, symptoms, emergency_name,emergency_number,emergency_email,= row

            # Append information to the scrolled text widget
            scroll_text.insert(tk.END, f"First Name: {first_name}\n"
                                      f"Second Name: {second_name}\n"
                                      f"Last Name: {last_name}\n"
                                      f"Age: {age}\n"
                                      f"Sex: {sex}\n"
                                      f"Address: {address}\n"
                                      f"Contact No.: {contact_number}\n"
                                      f"Email Address: {email}\n"
                                      f"Last Visited Place: {visited_recently}\n"
                                      f"Date of Visit: {date_of_visit}\n"
                                      f"COVID-19 Vaccination Status: {vaccine_status}\n"
                                      f"COVID-19 Test Result: {test_result}\n"
                                      f"Exposed to COVID-19 in the last 14 days? {close_contact}\n"
                                      f"Experiencing symptoms in the past 7 days?{symptoms}\n"
                                      f"Emergency Contact's Name: {emergency_name}\n"
                                      f"Emergency Contact Phone Number: {emergency_number}\n"
                                      f"Emergency Contact Email Address: {emergency_email}\n\n")

        # Disable editing in the scrolled text widget
        scroll_text.configure(state='disabled')

        result_window.mainloop()
