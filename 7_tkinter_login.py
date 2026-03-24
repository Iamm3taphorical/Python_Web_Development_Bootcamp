import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")
        self.root.geometry("350x220")
        self.root.resizable(False, False)

        # this is where the frame is designed 
        self.frame = tk.Frame(root, padx=20, pady=20)
        self.frame.pack(expand=True)

        # this is how we desing the title 
        tk.Label(self.frame, text="Login", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        # this is how we design the username 
        tk.Label(self.frame, text="Username:").grid(row=1, column=0, sticky="e", pady=5)
        self.entry_username = tk.Entry(self.frame, width=20)
        self.entry_username.grid(row=1, column=1, pady=5)

        # this is how we design the password 
        tk.Label(self.frame, text="Password:").grid(row=2, column=0, sticky="e", pady=5)
        self.entry_password = tk.Entry(self.frame, show="*", width=20)
        self.entry_password.grid(row=2, column=1, pady=5)

        # this is how we design the button 
        tk.Button(self.frame, text="Login", width=15, command=self.login).grid(row=3, column=0, columnspan=2, pady=15)

        # this is how we bind the enter key 
        self.root.bind('<Return>', lambda event: self.login())

    def login(self):
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()

        # here is where the validation proccess is made 
        if not username or not password:
            messagebox.showwarning("Input Error", "Please fill in all fields")
            return

        # this is the dummy authentication 
        if username == "admin" and password == "password":
            messagebox.showinfo("Login Success", f"Welcome, {username}!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

        # it clears the password after trying once 
        self.entry_password.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()