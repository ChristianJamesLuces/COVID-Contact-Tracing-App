# Import necessary modules
import tkinter as tk
from PIL import ImageTk, Image
from tracing_form import TracingForm
from tkinter import messagebox
import csv

# Create file handling class
class FileHandling():
    # Search the user's data
    def search_window(self):
        finder_window = tk.Toplevel()
        finder_window.title("Search Data")
        finder_window.geometry("800x400")
        finder_window.resizable(False, False)


        search_label = tk.Label(finder_window, text="Search Data", fg="black", font=("Arial", 15, "bold"))
        search_label.pack()

        # Create search entry
        self.search_entry = tk.Entry(finder_window)
        self.search_entry.pack(pady=10)

        # Create search result display
        search_result = tk.Listbox(finder_window, width=700, height=250)
        search_result.pack(pady=10)

        self.data_button(finder_window)
        self.update_button(finder_window)

    #Create button to search data
    def data_button(self, finder_window):
        image = Image.open("desing_elements/search_button.png")
        resized_image = image.resize((30, 30), Image.ANTIALIAS)
        button_image = ImageTk.PhotoImage(resized_image)
        search_data_button = tk.Button(finder_window, image=button_image, borderwidth=1, command=self.search_data)
        search_data_button.image = button_image 
        search_data_button.place(x=300, y=32)

    #Create button to update data
    def update_button(self, finder_window):
        update_buton = tk.Button(finder_window, text="Update",fg="green", font=("Time", 11, "bold"), command=self.update)
        update_buton.place(x=700, y=10)


    #Saving the user's data
    def search_data(self):
        search_keyword = self.search_entry.get()
        results = []
        with open("user_database.csv", "r", newline="", encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if search_keyword.lower() in " ".join(row).lower():
                    results.append(", ".join(row))
        return results

    #Saving the data if the user updates it
    def update(self, old_contact_data, new_contact_data):
        with open("user_database.csv", "r", newline="", encoding="utf-8") as file:
            data = list(csv.reader(file))

        with open("user_database.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            updated = False
            for row in data:
                if ", ".join(old_contact_data) == ", ".join(row):
                    writer.writerow(new_contact_data)
                    updated = True
                else:
                    writer.writerow(row)

            if updated:
                messagebox.showinfo("Success", "Data updated successfully.")
            else:
                messagebox.showwarning("Not Found", "Data not found for updating.")

