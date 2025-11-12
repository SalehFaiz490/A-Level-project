import tkinter as tk

def create_window():
    window = tk.Tk()

    window.geometry("400x300")

    user_name_entry_label = tk.Label(text="Enter User Name")
    user_name_entry_label.pack()

    user_name_entry = tk.Entry()
    user_name_entry.pack()


    password_entry_label = tk.Label(text="Enter Password")
    password_entry_label.pack()

    password_entry = tk.Entry()
    password_entry.pack()


    def enter_command():
        entries = get_entries()
        user_name = entries[0]
        password = entries[1]

        if user_name != "" and password != "":
            user_name_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            sucess_label.configure(text=f"You have Successfully been registered with username {user_name} \n "
                                        f"This window will close in 3 seconds")

            window.after(3000, window.destroy)

        return user_name, password

    def get_entries():
        return user_name_entry.get(), password_entry.get()


    sucess_label = tk.Label(text="")
    sucess_label.pack()

    enter_button = tk.Button(text="Enter", command=enter_command)
    enter_button.pack()


    window.mainloop()

