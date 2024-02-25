import tkinter as tk
from tkinter import messagebox
import pymssql

# Function to handle adding students
def add_student():
    x = 9

def view_students():
    try:
        # Establish a connection to the SQL Server database
        connection = pymssql.connect(server='Z4P5-NB003',
                                     user='sa',
                                     password='p@ssw0rd',
                                     database='sekolah')
        
        cursor = connection.cursor()

        # Execute a query to fetch student data from the database
        cursor.execute("SELECT id, name, phone FROM Students")

        # Fetch all rows from the result set
        students = cursor.fetchall()

        # Create a new window to display the student data
        student_window = tk.Toplevel()
        student_window.title("Students")

        # Create a Listbox widget to display student data
        student_listbox = tk.Listbox(student_window, width=50)
        student_listbox.pack(padx=10, pady=10)

        # Display the fetched student data in the Listbox
        if students:
            for student in students:
                student_info = f"ID: {student[0]}, Name: {student[1]}, Phone: {student[2]}"
                student_listbox.insert(tk.END, student_info)
        else:
            student_listbox.insert(tk.END, "No students available.")

        # Close the cursor and connection
        cursor.close()
        connection.close()

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def open_main_window():
    # Create main window
    main_window = tk.Tk()
    main_window.title("Paparan Utama")
    # Add widgets and functionalities for the main window here

    # Student Name Entry
    name_label = tk.Label(main_window, text="Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    name_entry = tk.Entry(main_window, width=30)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    # Student ID Entry
    id_label = tk.Label(main_window, text="ID:")
    id_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    id_entry = tk.Entry(main_window, width=30)
    id_entry.grid(row=1, column=1, padx=5, pady=5)

    # Add Student Button
    add_button = tk.Button(main_window, text="Add Student", command=add_student)
    add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    # View Students Button
    view_button = tk.Button(main_window, text="View Students", command=view_students)
    view_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    # Exit Button
    exit_button = tk.Button(main_window, text="Exit", command=main_window.destroy)
    exit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    # Center the window
    window_width = 300
    window_height = 200
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2
    main_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    main_window.mainloop()