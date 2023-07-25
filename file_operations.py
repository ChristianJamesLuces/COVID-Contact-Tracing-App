
#Import necessary modules
import tkinter as tk
from tkinter import messagebox
from tracing_form import TracingForm
import csv


#Create file handling class
class FileHandling():
    #Search the user's data
    def search_window(self):
        finder_window = tk.Toplevel()
        finder_window.title("Search Data")

        search_label = tk.Label(finder_window, text="Search Data", fg="black", font=("Arial", 15, "bold"))
        search_label.pack()

        # Create search entry
        search_entry = tk.Entry(finder_window)
        search_entry.pack(pady=10)

        # Create search result display
        search_result = tk.Listbox(finder_window, width=80)
        search_result.pack(pady=10)

    #Saving the user's data




