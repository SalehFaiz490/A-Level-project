import tkinter as tk
import database



class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x300")

        # username label
        self.username_label = tk.Label(text="Enter Username")
        self.username_label.pack()

        # username entry
        self.username_entry = tk.Entry()
        self.username_entry.pack()

        # password label
        self.password_label = tk.Label(text="Enter Password")
        self.password_label.pack()

        # password entry
        self.password_entry = tk.Entry()
        self.password_entry.pack()

        # enter button
        self.enter_button = tk.Button(text="Enter", command=self.enter_command)
        self.enter_button.pack()

        # sucess label:
        self.sucess_label = tk.Label(text="")
        self.sucess_label.pack()

        # data
        self.is_logged_in = False
        self.username = None
        self.user_id = None


    def enter_command(self):

        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.validate_entry_feilds(username, password):

            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)

            check = database.check_database(username, password)

            user_id = check[1]

            if check[0]:

                self.username = username
                self.user_id = user_id
                self.sucess_label.configure(text=f"Welcome Back {username}!!! \n"
                                                 f"This window will close after 3 seconds")

                self.window.after(3000, self.window.destroy)

                self.is_logged_in = True

            else:
                database.registor_new_user(username, password)

                self.username = username
                self.user_id = user_id

                self.sucess_label.configure(text=f"You have successfully been registered with username {username} \n"
                                                 f"This window will close after 3 seconds")

                self.window.after(3000, self.window.destroy)

                self.is_logged_in = True

    def validate_entry_feilds(self, username, password):

        if username == "" or password == "":
            self.sucess_label.configure(text="Fields cannot be empty")
            # entries must not be null
            return False

        elif len(username) > 48 or len(password) > 48:
            # length check to determine if username is less than 48 chars
            self.sucess_label.configure(text="Your Username or password were too long, cap = 48 characters")
            return False

        elif len(password) < 8:
            # password should be more than 8 chars
            self.sucess_label.configure(text="Your password was too short, must be at least 8 characters")
            return False

        user = database.collect_leaderboard_data()
        check = database.check_database(username, password)

        for i in range(0, len(user)):
            # checks if username and password match.
            if user[i][0] == username and not check[0]:

                # Checks if the username entered already exists in the database, username should be novel
                self.sucess_label.configure(text="Username already exists")
                return False

        return True


