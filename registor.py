import tkinter as tk
import database


class Window:
    """
    Handles a simple Tkinter login/registration window.
    - Users can enter a username and password.
    - If the username exists and password matches, logs in the user.
    - Otherwise, registers a new user automatically.
    """
    def __init__(self):
        # Create the main window
        self.window = tk.Tk()
        self.window.geometry("400x300")

        # Username input
        self.username_label = tk.Label(text="Enter Username")
        self.username_label.pack()

        self.username_entry = tk.Entry()
        self.username_entry.pack()

        # Password input
        self.password_label = tk.Label(text="Enter Password")
        self.password_label.pack()

        self.password_entry = tk.Entry()
        self.password_entry.pack()

        # Enter button
        self.enter_button = tk.Button(text="Enter", command=self.enter_command)
        self.enter_button.pack()

        # Feedback label
        self.sucess_label = tk.Label(text="")
        self.sucess_label.pack()

        # User data state
        self.is_logged_in = False
        self.username = None
        self.user_id = None

    # Button command
    def enter_command(self):
        """
        Called when the 'Enter' button is pressed.
        Validates input fields, then either logs in or registers the user.
        Provides feedback in the window and closes it after 3 seconds.
        """
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.validate_entry_feilds(username, password):
            # Clear the input fields after submission
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)

            check = database.check_database(username, password)
            user_id = check[1]

            if check[0]:
                # Existing user login
                self.username = username
                self.user_id = user_id
                self.sucess_label.configure(
                    text=f"Welcome Back {username}!!! \n"
                         f"This window will close after 3 seconds"
                )

                self.window.after(3000, self.window.destroy)
                self.is_logged_in = True
            else:
                # New user registration
                database.registor_new_user(username, password)
                self.username = username
                self.user_id = user_id
                self.sucess_label.configure(
                    text=f"You have successfully been registered with username {username} \n"
                         f"This window will close after 3 seconds"
                )

                self.window.after(3000, self.window.destroy)
                self.is_logged_in = True

    # Input validation
    def validate_entry_feilds(self, username, password):
        """
        Validates the username and password inputs.
        Checks:
        - Fields are not empty
        - Username and password lengths
        - Password minimum length
        - Username uniqueness in the database
        """
        if username == "" or password == "":
            self.sucess_label.configure(text="Fields cannot be empty")
            return False

        elif len(username) > 45 or len(password) > 45:
            self.sucess_label.configure(
                text="Your Username or password were too long, cap = 45 characters"
            )
            return False

        elif len(password) < 8:
            self.sucess_label.configure(
                text="Your password was too short, must be at least 8 characters"
            )
            return False

        # Get existing users from the database
        user = database.collect_leaderboard_data()
        check = database.check_database(username, password)

        for i in range(len(user)):
            # Prevent registering a username that already exists
            if user[i][0] == username and not check[0]:
                self.sucess_label.configure(text="Username already exists")
                return False

        return True
