
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import csv



class FileHandler():
    #Create a search window
    def search_window(self):
        self.first_search_window = tk.Tk()
        self.first_search_window.title("Search Contact - CoviCompanion")
        self.first_search_window.geometry("400x100")

        search_label = tk.Label(self.first_search_window, text="Enter the First Name to search:", font=("Arial", 12, "bold"))
        search_label.pack()

        self.search_entry = tk.Entry(self.first_search_window, font=("Arial", 12))
        self.search_entry.place(x=100, y=40)
        self.search_button(self.first_search_window)

    #Create a search button
    def search_button(self, first_search_window):
        search_button = tk.Button(self.first_search_window, text="Search", command=self.search_contact)
        search_button.place(x=50, y=40)

        self.result_label = tk.Label(self.first_search_window, text="", font=("Arial", 12))
        self.result_label.place(x=100, y=70)
    
    #Search the data
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
        self.result_window = tk.Toplevel()
        self.result_window.title("Search Results - CoviCompanion")
        self.result_window.geometry("800x400")
        self.result_window.resizable(False,False)

        result_label = tk.Label(self.result_window, text="Search Results:", font=("Arial", 15, "bold"))
        result_label.pack()

        # Create a scrolled text widget for displaying search results
        scroll_text = scrolledtext.ScrolledText(self.result_window, wrap=tk.WORD, width=100, height=20)
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
            
            # Add Edit button for each row
            edit_button = tk.Button(self.result_window, text="Edit", command=lambda r=row: self.edit_data(r), font=("Time", 12, "bold") , fg="green")
            edit_button.place(x=750, y=362)

            # Add Remove button for each row
            remove_button = tk.Button(self.result_window, text="Remove", command=lambda r=row: self.remove_data(r),  font=("Time", 12, "bold"), fg="red")
            remove_button.place(x=20, y=362)

        # Disable editing in the scrolled text widget
        scroll_text.configure(state='disabled')

        self.result_window.mainloop()
    
    # Remove the data 
    def remove_data(self, data_row):
        with open("contact_list.csv", "r", newline="") as file:
            rows = [row for row in csv.reader(file)]

        index_to_remove = rows.index(data_row)

        del rows[index_to_remove]

        with open("contact_list.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        
        # Display a message after successful removal
        messagebox.showinfo("Success", "Data removed successfully.")

        # Close the result window after removing data
        self.result_window.destroy()
        self.first_search_window.destroy()
        
    # Edit the specified data
    def edit_data(self, data_row):
        self.edit_window = tk.Toplevel()
        self.edit_window.title("Edit Data - CoviCompanion")
        self.edit_window.geometry("900x400")

        first_name_var = tk.StringVar(self.edit_window, value=data_row[0])
        second_name_var = tk.StringVar(self.edit_window, value=data_row[1])
        last_name_var = tk.StringVar(self.edit_window, value=data_row[2])
        age_var = tk.StringVar(self.edit_window, value=data_row[3])
        sex_var = tk.StringVar(self.edit_window, value=data_row[4])
        address_var = tk.StringVar(self.edit_window, value=data_row[5])
        contact_number_var = tk.StringVar(self.edit_window, value=data_row[6])
        email_var = tk.StringVar(self.edit_window, value=data_row[7])
        visited_recently_var = tk.StringVar(self.edit_window, value=data_row[8])
        date_of_visit_var = tk.StringVar(self.edit_window, value=data_row[9])
        vaccine_status_var = tk.StringVar(self.edit_window, value=data_row[10])
        test_result_var = tk.StringVar(self.edit_window, value=data_row[11])
        close_contact_var = tk.StringVar(self.edit_window, value=data_row[12])
        symptoms_var = tk.StringVar(self.edit_window, value=data_row[13])
        emergency_name_var = tk.StringVar(self.edit_window, value=data_row[14])
        emergency_number_var = tk.StringVar(self.edit_window, value=data_row[15])
        emergency_email_var = tk.StringVar(self.edit_window, value=data_row[16])

        tk.Label(self.edit_window, text="First Name:").grid(row=0, column=0, padx=5, pady=10)
        first_name_entry = tk.Entry(self.edit_window, textvariable=first_name_var)
        first_name_entry.grid(row=0, column=1)

        tk.Label(self.edit_window, text="Second Name:").grid(row=1, column=0, padx=5, pady=10)
        second_name_entry = tk.Entry(self.edit_window, textvariable=second_name_var)
        second_name_entry.grid(row=1, column=1)

        tk.Label(self.edit_window, text="Last Name:").grid(row=2, column=0, padx=5, pady=10)
        last_name_entry = tk.Entry(self.edit_window, textvariable=last_name_var)
        last_name_entry.grid(row=2, column=1)

        tk.Label(self.edit_window, text="Age:").grid(row=3, column=0, padx=5, pady=10)
        age_entry = tk.Entry(self.edit_window, textvariable=age_var)
        age_entry.grid(row=3, column=1)

        tk.Label(self.edit_window, text="Sex (male,female,intersex):").grid(row=4, column=0, padx=5, pady=10)
        sex_entry = tk.Entry(self.edit_window, textvariable=sex_var)
        sex_entry.grid(row=4, column=1)

        tk.Label(self.edit_window, text="Address:").grid(row=5, column=0, padx=5, pady=10)
        address_entry = tk.Entry(self.edit_window, textvariable=address_var)
        address_entry.grid(row=5, column=1)

        tk.Label(self.edit_window, text="Contact Number:").grid(row=6, column=0, padx=5, pady=10)
        contact_number_entry = tk.Entry(self.edit_window, textvariable=contact_number_var)
        contact_number_entry.grid(row=6, column=1)

        tk.Label(self.edit_window, text="Email Address:").grid(row=7, column=0, padx=5, pady=10)
        email_entry = tk.Entry(self.edit_window, textvariable=email_var)
        email_entry.grid(row=7, column=1)

        tk.Label(self.edit_window, text="Last Visited Place:").grid(row=8, column=0, padx=5, pady=10)
        visited_recently_entry = tk.Entry(self.edit_window, textvariable=visited_recently_var)
        visited_recently_entry.grid(row=8, column=1)

        tk.Label(self.edit_window, text="Date of Visit:").grid(row=0, column=2, padx=5, pady=10)
        date_of_visit_entry = tk.Entry(self.edit_window, textvariable=date_of_visit_var)
        date_of_visit_entry.grid(row=0, column=3)

        tk.Label(self.edit_window, text="COVID-19 Vaccination Status:").grid(row=1, column=2, padx=5, pady=10)
        vaccine_status_entry = tk.Entry(self.edit_window, textvariable=vaccine_status_var)
        vaccine_status_entry.grid(row=1, column=3)

        tk.Label(self.edit_window, text="COVID-19 Test Result:").grid(row=2, column=2, padx=5, pady=10)
        test_result_entry = tk.Entry(self.edit_window, textvariable=test_result_var)
        test_result_entry.grid(row=2, column=3)

        tk.Label(self.edit_window, text="Exposed to COVID-19 in the last 14 days?").grid(row=3, column=2, padx=5, pady=10)
        close_contact_entry = tk.Entry(self.edit_window, textvariable=close_contact_var)
        close_contact_entry.grid(row=3, column=3)

        tk.Label(self.edit_window, text="Experiencing symptoms in the past 7 days?").grid(row=4, column=2, padx=5, pady=10)
        symptoms_entry = tk.Entry(self.edit_window, textvariable=symptoms_var)
        symptoms_entry.grid(row=4, column=3)

        tk.Label(self.edit_window, text="Emergency Contact's Name:").grid(row=5, column=2, padx=5, pady=10)
        emergency_name_entry = tk.Entry(self.edit_window, textvariable=emergency_name_var)
        emergency_name_entry.grid(row=5, column=3)

        tk.Label(self.edit_window, text="Emergency Contact Phone Number:").grid(row=6, column=2, padx=5, pady=10)
        emergency_number_entry = tk.Entry(self.edit_window, textvariable=emergency_number_var)
        emergency_number_entry.grid(row=6, column=3)

        tk.Label(self.edit_window, text="Emergency Contact Email Address:").grid(row=7, column=2, padx=5, pady=10)
        emergency_email_entry = tk.Entry(self.edit_window, textvariable=emergency_email_var)
        emergency_email_entry.grid(row=7, column=3)

        save_button = tk.Button(self.edit_window, text="Save", fg= "blue",  font=("Time", 12, "bold"), command=lambda: self.save_edited_data(
            data_row,
            first_name_var.get().lower(),
            second_name_var.get().lower(),
            last_name_var.get().lower(),
            age_var.get().lower(),
            sex_var.get().lower(),
            address_var.get().lower(),
            contact_number_var.get().lower(),
            email_var.get().lower(),
            visited_recently_var.get().lower(),
            date_of_visit_var.get().lower(),
            vaccine_status_var.get().lower(),
            test_result_var.get().lower(),
            close_contact_var.get().lower(),
            symptoms_var.get().lower(),
            emergency_name_var.get().lower(),
            emergency_number_var.get().lower(),
            emergency_email_var.get().lower()
        ))
        save_button.place(x=800, y=350)

    def save_edited_data(self, old_data, new_first_name, new_second_name, new_last_name, new_age, new_sex, new_address,
                     new_contact_number, new_email, new_visited_recently, new_date_of_visit, new_vaccine_status,
                     new_test_result, new_close_contact, new_symptoms, new_emergency_name, new_emergency_number,
                     new_emergency_email):
        with open("contact_list.csv", "r", newline="") as file:
            rows = [row for row in csv.reader(file)]

        index_to_edit = rows.index(old_data)

        rows[index_to_edit] = [new_first_name, new_second_name, new_last_name, new_age, new_sex, new_address,
                           new_contact_number, new_email, new_visited_recently, new_date_of_visit, new_vaccine_status,
                           new_test_result, new_close_contact, new_symptoms, new_emergency_name, new_emergency_number,
                           new_emergency_email]

        with open("contact_list.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        # Close the edit window after saving
        messagebox.showinfo("Success", "Data edited successfully.")
        self.edit_window.destroy()
        self.result_window.destroy()