import tkinter as tk
from tkinter import messagebox

# -------------------- Main Window --------------------
root = tk.Tk()
root.title("Contact Management System")
root.geometry("900x500")
root.config(bg="#f4f6f8")

contacts = []

# -------------------- Styles --------------------
TITLE_FONT = ("Segoe UI", 20, "bold")
LABEL_FONT = ("Segoe UI", 10)
ENTRY_FONT = ("Segoe UI", 10)
BTN_FONT = ("Segoe UI", 10, "bold")
LIST_FONT = ("Segoe UI", 10)

BG_COLOR = "#f4f6f8"
CARD_COLOR = "#ffffff"
PRIMARY_COLOR = "#2563eb"
DANGER_COLOR = "#dc2626"
TEXT_COLOR = "#111827"

# -------------------- Functions --------------------
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def refresh_list():
    contact_list.delete(0, tk.END)
    for c in contacts:
        contact_list.insert(tk.END, f"{c['name']}  |  {c['phone']}")

def add_contact():
    contact = {
        "name": name_entry.get(),
        "phone": phone_entry.get(),
        "email": email_entry.get(),
        "address": address_entry.get()
    }
    if contact["name"] == "" or contact["phone"] == "":
        messagebox.showwarning("Warning", "Name and Phone are required")
        return
    contacts.append(contact)
    refresh_list()
    clear_entries()

def select_contact(event):
    try:
        index = contact_list.curselection()[0]
        c = contacts[index]
        clear_entries()
        name_entry.insert(0, c["name"])
        phone_entry.insert(0, c["phone"])
        email_entry.insert(0, c["email"])
        address_entry.insert(0, c["address"])
    except:
        pass

def update_contact():
    try:
        index = contact_list.curselection()[0]
        contacts[index] = {
            "name": name_entry.get(),
            "phone": phone_entry.get(),
            "email": email_entry.get(),
            "address": address_entry.get()
        }
        refresh_list()
        clear_entries()
    except:
        messagebox.showwarning("Warning", "Select a contact to update")

def delete_contact():
    try:
        index = contact_list.curselection()[0]
        contacts.pop(index)
        refresh_list()
        clear_entries()
    except:
        messagebox.showwarning("Warning", "Select a contact to delete")

def search_contact():
    keyword = search_entry.get().lower()
    contact_list.delete(0, tk.END)
    for c in contacts:
        if keyword in c["name"].lower() or keyword in c["phone"]:
            contact_list.insert(tk.END, f"{c['name']}  |  {c['phone']}")

# -------------------- UI Layout --------------------
# Title
tk.Label(root, text="Contact Management System",
         font=TITLE_FONT, bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)

main_frame = tk.Frame(root, bg=BG_COLOR)
main_frame.pack(fill="both", expand=True, padx=20)

# -------------------- Left Card --------------------
left_card = tk.Frame(main_frame, bg=CARD_COLOR, bd=0)
left_card.pack(side="left", fill="both", expand=True, padx=10)

tk.Label(left_card, text="Contact Details",
         font=("Segoe UI", 14, "bold"),
         bg=CARD_COLOR).pack(pady=10)

def field(label):
    tk.Label(left_card, text=label, bg=CARD_COLOR,
             font=LABEL_FONT).pack(anchor="w", padx=20)

def entry():
    e = tk.Entry(left_card, font=ENTRY_FONT)
    e.pack(fill="x", padx=20, pady=5)
    return e

field("Name")
name_entry = entry()

field("Phone")
phone_entry = entry()

field("Email")
email_entry = entry()

field("Address")
address_entry = entry()

btn_frame = tk.Frame(left_card, bg=CARD_COLOR)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add",
          bg=PRIMARY_COLOR, fg="white",
          font=BTN_FONT, width=10,
          command=add_contact).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Update",
          bg="#059669", fg="white",
          font=BTN_FONT, width=10,
          command=update_contact).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Delete",
          bg=DANGER_COLOR, fg="white",
          font=BTN_FONT, width=10,
          command=delete_contact).grid(row=0, column=2, padx=5)

# -------------------- Right Card --------------------
right_card = tk.Frame(main_frame, bg=CARD_COLOR)
right_card.pack(side="right", fill="both", expand=True, padx=10)

tk.Label(right_card, text="Contact List",
         font=("Segoe UI", 14, "bold"),
         bg=CARD_COLOR).pack(pady=10)

search_entry = tk.Entry(right_card, font=ENTRY_FONT)
search_entry.pack(fill="x", padx=20)

tk.Button(right_card, text="Search",
          bg=PRIMARY_COLOR, fg="white",
          font=BTN_FONT,
          command=search_contact).pack(pady=5)

contact_list = tk.Listbox(right_card, font=LIST_FONT)
contact_list.pack(fill="both", expand=True, padx=20, pady=10)
contact_list.bind("<<ListboxSelect>>", select_contact)

# -------------------- Run App --------------------
root.mainloop()
