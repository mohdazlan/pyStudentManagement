import tkinter as tk
from tkinter import messagebox
import pymssql

# Function to handle adding students
def add_student():
    x = 9
def update_student(student_id):
    # Create a new window for updating student information
    update_window = tk.Toplevel()
    update_window.title("Update Student")

    # Label and Entry for student name
    name_label = tk.Label(update_window, text="Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    name_entry = tk.Entry(update_window, width=30)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    # Label and Entry for student ID
    id_label = tk.Label(update_window, text="ID:")
    id_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    id_entry = tk.Entry(update_window, width=30)
    id_entry.grid(row=1, column=1, padx=5, pady=5)

    # Button to update student information
    update_button = tk.Button(update_window, text="Update", command=lambda: perform_update(student_id, name_entry.get(), id_entry.get()))
    update_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    # Function to perform the update operation
    def perform_update(student_id, new_name, new_id):
        try:
            # Establish a connection to the SQL Server database
            connection = pymssql.connect(server='your_server_name',
                                         user='your_username',
                                         password='your_password',
                                         database='your_database_name')
            cursor = connection.cursor()

            # Execute an SQL UPDATE statement to update the student information
            cursor.execute("UPDATE Students SET student_name = %s, id = %s WHERE student_id = %s", (new_name, new_id, student_id))
            connection.commit()

            # Close the cursor and connection
            cursor.close()
            connection.close()

            # Show success message
            messagebox.showinfo("Success", "Student information updated successfully!")

            # Close the update window
            update_window.destroy()
        except Exception as e:
            # Show error message if an error occurs
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to handle deleting a student
def delete_student(student_id):
    # Prompt the user for confirmation before deleting the student
    confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to delete this student?")
    if confirmed:
        try:
            # Establish a connection to the SQL Server database
            connection = pymssql.connect(server='Z4P5-NB003', user='sa', password='p@ssw0rd',database='sekolah')
            cursor = connection.cursor()

            # Execute an SQL DELETE statement to delete the student from the database
            cursor.execute("DELETE FROM Students WHERE id = %s", (student_id,))
            connection.commit()

            # Close the cursor and connection
            cursor.close()
            connection.close()

            # Show success message
            messagebox.showinfo("Success", "Student deleted successfully!")
        except Exception as e:
            # Show error message if an error occurs
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


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
            #for student in students:
            #    student_info = f"ID: {student[0]}, Name: {student[1]}, Phone: {student[2]}"
            #    student_listbox.insert(tk.END, student_info)
            for student in students:
                student_info = f"ID: {student[0]}, Name: {student[1]}, Phone: {student[2]}"
                student_listbox.insert(tk.END, student_info)
            # Add update and delete buttons for each student
            update_button = tk.Button(student_window, text="Update", command=lambda sid=student[0]: update_student(sid))
            update_button.pack()
            delete_button = tk.Button(student_window, text="Delete", command=lambda sid=student[0]: delete_student(sid))
            delete_button.pack()
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
    id_label = tk.Label(main_window, text="Phone:")
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