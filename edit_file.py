
import tkinter as tk
from tkinter import scrolledtext
from PIL import ImageTk, Image
import csv



class FileHandler():
    #Create a search window
    def search_window(self):
        search_window = tk.Tk()
        search_window.title("Search Contact - CoviCompanion")
        search_window.geometry("400x100")

        search_label = tk.Label(search_window, text="Enter the First Name to search:", font=("Arial", 12, "bold"))
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
