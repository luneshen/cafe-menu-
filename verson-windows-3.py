from tkinter import *
from tkinter import messagebox
from datetime import datetime

# Main function to initialize the login window
def main():
    global root
    root = Tk()
    root.title("Login")
    root.geometry("700x200")

    # Set background image
    background_image = PhotoImage(file="C:\\Users\\HP\\Documents\\python\\2023\\image\\bdsc.png")
    background_label = Label(root, image=background_image)
    background_label.grid(row=0, column=0, columnspan=3)

    # Create buttons for signing in, signing up, and exiting
    btnaddaccount = Button(root, text="Sign in", command=check_account)
    btnaddaccount.grid(row=1, column=0, pady=1)

    btnsrchaccount = Button(root, text="Sign up", command=add_account)
    btnsrchaccount.grid(row=1, column=1, pady=1)

    btnexit = Button(root, text="Exit", command=close_window)
    btnexit.grid(row=1, column=2, pady=1)

    root.mainloop()

# Function to check user account credentials for signing in
def check_account():
    global checking_account_window
    checking_account_window = Toplevel(root)
    checking_account_window.title("Sign in")
    checking_account_window.geometry("300x150")

    # Create labels and entry fields for username and password
    account_label = Label(checking_account_window, text="Enter account name:")
    account_label.grid(row=0, column=0)
    account_entry = Entry(checking_account_window)
    account_entry.grid(row=0, column=1)

    password_label = Label(checking_account_window, text="Enter password:")
    password_label.grid(row=1, column=0)
    password_entry = Entry(checking_account_window, show="*")
    password_entry.grid(row=1, column=1)

    # Create buttons for submitting account credentials and password recovery
    checking_button = Button(checking_account_window, text="Done",
                             command=lambda: checking_password(account_entry.get(), password_entry.get()))
    checking_button.grid(row=2, column=0)

    search_button = Button(checking_account_window, text="Forget password", command=search_account)
    search_button.grid(row=2, column=1)

# Function to validate the user's password for signing in
def checking_password(username, password):
    with open("passwords.txt", "r") as f:
        for line in f:
            account, stored_password = line.strip().split(":")
            if (account == username and stored_password == password) or (account == password and stored_password == username):
                messagebox.showinfo("Success", "Login successful!")
                cafe_menu()
                checking_account_window.destroy()
                return
        messagebox.showerror("Error", "Invalid username or password!")

# Function to create a new user account
def add_account():
    global add_account_window
    add_account_window = Toplevel(root)
    add_account_window.title("Sign up")
    add_account_window.geometry("300x200")

    # Create labels and entry fields for username and password
    account_label = Label(add_account_window, text="Enter account name: ")
    account_label.grid(row=0, column=0)
    account_entry = Entry(add_account_window)
    account_entry.grid(row=0, column=1)

    password_label = Label(add_account_window, text="Enter password: ")
    password_label.grid(row=1, column=0)
    password_entry = Entry(add_account_window, show="*")
    password_entry.grid(row=1, column=1)

    # Create a button to save the new account
    save_button = Button(add_account_window, text="Save", command=lambda: save_account(account_entry, password_entry))
    save_button.grid(row=3, columnspan=2)

# Function to save the new user account to a file
def save_account(account_entry, password_entry):
    account = account_entry.get()
    password = password_entry.get()
    with open("passwords.txt", "a") as f:
        f.write(f"{account}:{password}\n")
    add_account_window.destroy()
    messagebox.showinfo("Success", "Account created!")

# Function for password recovery
def search_account():
    def find_password():
        username = search_entry.get()

        with open("passwords.txt", "r") as f:
            for line in f:
                account, password = line.strip().split(":")
                if account == username:
                    messagebox.showinfo("Password Recovery", f"Your password is: {password}")
                    return

        messagebox.showerror("Error", "Account not found!")

    search_account_window = Toplevel(root)
    search_account_window.title("Password Recovery")
    search_account_window.geometry("300x150")

    # Create labels and entry field for username
    search_label = Label(search_account_window, text="Enter account name:")
    search_label.grid(row=0, column=0)
    search_entry = Entry(search_account_window)
    search_entry.grid(row=0, column=1)

    # Create a button to find the password
    search_button = Button(search_account_window, text="Find Password", command=find_password)
    search_button.grid(row=1, columnspan=2)

# Function to close the main window
def close_window():
    root.destroy()

# Café menu dictionary with items and prices
menu = {
    "Coffee": 3.5,
    "Tea": 4.0,
    "Sandwich": 7.0,
    "Salad": 4.5,
    "Cake": 3.0,
    "Milktea":5.0,
    "Egg tart":3.0,
    "Any soda drink":4.0,
    "Smoothie":6.0,
    "Steak":8.0,
    "Cocktail":6.0,
    "Sausage roll":4.0,
    "Lasagna":5.0,
    "Pasta":6.0,
    "Bacon&eggs":7.0,
    "Taco":6.0,
    "Fish&chips":7.0,
    "Ice cream":4.0,
    "Garlic bread":5.0
}

# Function to display the café menu
def cafe_menu():
    global cafe_menu_window, selected_items, cart_items

    cafe_menu_window = Toplevel(root)
    cafe_menu_window.title("Menu")
    cafe_menu_window.geometry("500x400")

    # Create a frame for the menu listbox
    menu_frame = Frame(cafe_menu_window)
    menu_frame.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = Scrollbar(menu_frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    menu_listbox = Listbox(menu_frame, yscrollcommand=scrollbar.set)
    menu_listbox.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar.config(command=menu_listbox.yview)

    # Populate the menu listbox with menu items and prices
    for item, price in menu.items():
        menu_listbox.insert(END, f"{item}: ${price:.2f}")

    selected_items = []
    cart_items = {}

    # Create a frame for the cart listbox and other buttons
    cart_frame = Frame(cafe_menu_window)
    cart_frame.pack(side=RIGHT, fill=BOTH, expand=True)

    cart_label = Label(cart_frame, text="Cart")
    cart_label.pack()

    cart_listbox = Listbox(cart_frame)
    cart_listbox.pack(side=LEFT, fill=BOTH, expand=True)

    def update_cart():
        cart_listbox.delete(0, END)
        for item, quantity in cart_items.items():
            cart_listbox.insert(END, f"{item} x {quantity}")

    def calculate_total():
        total = sum([menu[item.split(':')[0].strip()] * quantity for item, quantity in cart_items.items()])
        total_label.config(text=f"Total: ${total:.2f}")

    def add_to_cart():
        selection = menu_listbox.curselection()
        if selection:
            item = menu_listbox.get(selection)
            selected_items.append(item)
            if item in cart_items:
                cart_items[item] += 1
            else:
                cart_items[item] = 1
            update_cart()
            calculate_total()

    def check_out():
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        with open("order_records.txt", "a") as f:
            f.write(f"Order placed at: {current_time}\n")
            for item, quantity in cart_items.items():
                f.write(f"{item} x {quantity}\n")
            f.write("\n")
        messagebox.showinfo("Successfully checked out", "Thank you for shopping!")
        cart_listbox.delete(0, END)
        cart_items.clear()
        calculate_total()

    def cancel_order():
        cart_listbox.delete(0, END)
        cart_items.clear()
        calculate_total()

    def logout():
        cafe_menu_window.withdraw()
        root.deiconify()

    # Create buttons for adding to cart, checking out, canceling order, and logging out
    add_to_cart_button = Button(cafe_menu_window, text="Add to Cart", command=add_to_cart)
    add_to_cart_button.pack()

    total_label = Label(cafe_menu_window, text="Total: $0.00")
    total_label.pack()

    check_out_button = Button(cafe_menu_window, text="Check Out", command=check_out)
    check_out_button.pack()

    cancel_order_button = Button(cafe_menu_window, text="Cancel Order", command=cancel_order)
    cancel_order_button.pack()

    logout_button = Button(cafe_menu_window, text="Logout", command=logout)
    logout_button.pack()

# Main function to initialize the GUI
if __name__ == "__main__":
    main()

