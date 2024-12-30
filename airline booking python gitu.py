import tkinter as tk
from tkinter import messagebox

class AirlineReservationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Airline Reservation System")
        
        self.name_label = tk.Label(root, text="Enter your name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        
        self.destination_label = tk.Label(root, text="Select destination:")
        self.destination_label.pack()
        self.destination_var = tk.StringVar()
        self.destination_var.set("New York")  # Default destination
        self.destination_menu = tk.OptionMenu(root, self.destination_var, "New York", "London", "Paris", "Tokyo")
        self.destination_menu.pack()
        
        self.class_label = tk.Label(root, text="Select class:")
        self.class_label.pack()
        self.class_var = tk.StringVar()
        self.class_var.set("Economy")  # Default class
        self.class_menu = tk.OptionMenu(root, self.class_var, "Economy", "Business", "First Class")
        self.class_menu.pack()
        
        self.book_button = tk.Button(root, text="Book Flight", command=self.book_flight)
        self.book_button.pack()
    
    def book_flight(self):
        name = self.name_entry.get()
        destination = self.destination_var.get()
        flight_class = self.class_var.get()
        messagebox.showinfo("Booking Confirmed", f"Hello, {name}!\nYour flight to {destination} in {flight_class} class has been booked!")

if __name__ == "__main__":
    root = tk.Tk()
    app = AirlineReservationSystem(root)
    root.mainloop()
