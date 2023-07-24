#Import necessary modules
from tkinter import *
from tkinter import messagebox

#Create a contact form/ tracing form class
class TracingForm():
    def __init__(self):
        self.user_information_window = Tk()
        self.user_information_window.title("Personal Data")
        self.user_information_window.geometry("1250x650")
        self.user_information_window.config(bg="#ECDADD")
        self.user_information_window.resizable(False,False)

    #Saving User's Information Label
    def user_information(self): 
        #Get name
        self.first_name = Label(self.user_information_window, text="First Name: ", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.first_name.grid(row=0, column=0, padx=5, pady=10)
        self.entry_first_name = Entry(self.user_information_window)
        self.entry_first_name.grid(row=0, column=1)
        
        self.second_name = Label(self.user_information_window, text="Second Name: ", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.second_name.grid(row=0, column=2, padx=5, pady=10)
        self.entry_second_name = Entry(self.user_information_window)
        self.entry_second_name.grid(row=0, column=3)
        
        self.last_name = Label(self.user_information_window, text="Last Name: ", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.last_name.grid(row=0, column=4, padx=5, pady=10)
        self.entry_last_name = Entry(self.user_information_window)
        self.entry_last_name.grid(row=0, column=5)
        
        #Get age 
        self.age = Label(self.user_information_window, text="Age (yrs. old):", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.age.grid(row=1, column=0, padx=5, pady=10)
        self.entry_age = Entry(self.user_information_window)
        self.entry_age.grid(row=1, column=1)
        
        #Get sex
        self.sex = Label(self.user_information_window, text="Sex:", font=("Arial", 9, "bold"), bg="#ECDADD")
        self.sex.grid(row=2, column=0, padx=5, pady=10)
        
        self.sex_radio = StringVar()
        self.male_sex = Radiobutton(self.user_information_window,variable=self.sex_radio, text="male", value=1, bg="#ECDADD")
        self.male_sex.grid(row=2, column=1)
        
        self.female_sex = Radiobutton(self.user_information_window, variable=self.sex_radio, text="female", value=2, bg="#ECDADD")
        self.female_sex.grid(row=2, column=2)
        
        self.inter_sex = Radiobutton(self.user_information_window, variable=self.sex_radio, text="intersex", value=3, bg="#ECDADD")
        self.inter_sex.grid(row=2, column=3)
        

        #Creat a submit button
        submit_button = Button(self.user_information_window, text="Submit", command=self.save_contact, fg="green", font=("Time", 11, "bold"))
        submit_button.place(x=1150, y=600)

        self.user_information_window.mainloop()

    #Save the contact
    def save_contact(self):
        first_name = self.entry_first_name.get()
        second_name = self.entry_second_name.get()
        last_name = self.entry_last_name.get()
        age = self.entry_age.get()
        sex = self.sex_radio.get()
       

        print(
            "First_Name", first_name,
            "\nSecond_Name", second_name,
            "\nLast_Name", last_name,
            "\nAge", age,
            "\nSex", sex,
         )
            

       
        
    
      


    

