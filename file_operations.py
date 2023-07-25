# Import necessary modules
import tkinter as tk
from PIL import ImageTk, Image
from tracing_form import TracingForm

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
        search_result = tk.Listbox(finder_window, width=700, height=300)
        search_result.pack(pady=10)

        self.data_button(finder_window)

    def data_button(self, finder_window):
        image = Image.open("desing_elements/search_button.png")
        resized_image = image.resize((30, 30), Image.ANTIALIAS)
        button_image = ImageTk.PhotoImage(resized_image)
        search_data_button = tk.Button(finder_window, image=button_image, borderwidth=0, command=self.search_data)
        search_data_button.image = button_image  # Store reference to prevent garbage collection
        search_data_button.place(x=200, y=15)


    # Saving the user's data
    def search_data(self):
        search_keyword = self.search_entry.get()
        results = []
        with open("user_database.csv", "r", newline="", encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if search_keyword.lower() in " ".join(row).lower():
                    results.append(", ".join(row))
        return results



