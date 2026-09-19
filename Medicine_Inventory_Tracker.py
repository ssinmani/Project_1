
from datetime import datetime
import json


# -----------------------------
# LOAD INVENTORY FROM JSON
# -----------------------------

def load_inventory():
    with open("inventory.json", "r") as file:
        data = json.load(file)
    return data


# -----------------------------
# MEDICINE CLASS
# -----------------------------

class Medicine:

    def __init__(self, Medicine_ID, Medicine_name, Category,
                 Quantity, Price, Expiry_date):

        self.Medicine_ID = Medicine_ID
        self.Medicine_name = Medicine_name
        self.Category = Category
        self.Quantity = Quantity
        self.Price = Price
        self.Expiry_date = Expiry_date

    def display(self):
        print("Medicine ID:", self.Medicine_ID)
        print("Medicine_name:", self.Medicine_name)
        print("Category:", self.Category)
        print("Quantity:", self.Quantity)
        print("Price:", self.Price)
        print("Expiry:", self.Expiry_date)

    def add_stock(self, amount):
        new_quantity = amount + self.Quantity
        self.Quantity = new_quantity
        return new_quantity

    def sell_stock(self, amount):
        new_quantity = self.Quantity - amount
        self.Quantity = new_quantity
        return new_quantity

    def check_low_stock(self):
        if self.Quantity < 30:
            print("Low Stock")
        else:
            print("Stock is sufficient")


# -----------------------------
# CONVERT JSON DATA
# INTO MEDICINE OBJECTS
# -----------------------------

def create_inventory(data):

    inventory = []

    for medicine in data:

        new_medicine = Medicine(
            medicine["Medicine_ID"],
            medicine["Medicine_name"],
            medicine["Category"],
            medicine["Quantity"],
            medicine["Price"],
            medicine["Expiry_date"]
        )

        inventory.append(new_medicine)

    return inventory


# -----------------------------
# GET MEDICINE ID
# -----------------------------

def get_medicine_id():

    n = int(input("Enter the medicine Id:"))
    return n


# -----------------------------
# SEARCH MEDICINE
# -----------------------------

def search_medicine(inventory, medicine_ID):

    found = False

    for medicine in inventory:

        if medicine_ID == medicine.Medicine_ID:

            found = True
            print("Medicine Found:", medicine.Medicine_name)

    if found == True:
        print("Medicine Found")
    else:
        print("Not Found")


# -----------------------------
# DELETE MEDICINE
# -----------------------------

def delete_medicine(inventory, medicine_ID):

    for medicine in inventory:

        if medicine_ID == medicine.Medicine_ID:

            inventory.remove(medicine)
            print("Medicine Delete:", medicine.Medicine_name)
            break


# -----------------------------
# UPDATE MEDICINE
# -----------------------------

def update_medicine(inventory, medicine_ID):

    for medicine in inventory:

        if medicine_ID == medicine.Medicine_ID:

            medicine.Price = 6

            print(
                "Medicine New Price:",
                medicine.Medicine_name,
                "New Price:",
                medicine.Price
            )


# -----------------------------
# CHECK EXPIRY
# -----------------------------

def expiry_medicine(inventory):

    today_date = datetime.now().date()

    for medicine in inventory:

        expiry_date = datetime.strptime(
            medicine.Expiry_date,
            "%m/%d/%Y"
        ).date()

        if expiry_date <= today_date:
            print("Expired:", medicine.Medicine_name)

        else:
            print("Not Expired:", medicine.Medicine_name)


# -----------------------------
# CHECK LOW STOCK
# -----------------------------

def check_low_stock(inventory):

    for medicine in inventory:

        if medicine.Quantity < 30:
            print("Low Stock:", medicine.Medicine_name)

        else:
            print("Stock is sufficient:", medicine.Medicine_name)


# -----------------------------
# CREATE INVENTORY
# FROM JSON
# -----------------------------

inventory_data = load_inventory()

inventory = create_inventory(inventory_data)


# -----------------------------
# MENU
# -----------------------------

def menu():

    print("1. Display medicines")
    print("2. Search medicine")
    print("3. Add stock")
    print("4. Sell medicine")
    print("5. Delete medicine")
    print("6. Update medicine")
    print("7. Check expiry")
    print("8. Check low stock")
    print("9. Exit")

    choice = input("Enter your choice: ")

    return choice


# -----------------------------
# MAIN PROGRAM
# -----------------------------

while True:

    choice = menu()

    if choice == "1":

        for medicine in inventory:
            medicine.display()


    elif choice == "2":

        medicine_id = get_medicine_id()

        search_medicine(inventory, medicine_id)


    elif choice == "3":

        medicine_id = get_medicine_id()

        amount = int(input("How many medicine to add: "))

        if amount <= 0:

            print("Invalid Amount")

        else:

            for medicine in inventory:

                if medicine.Medicine_ID == medicine_id:

                    medicine.add_stock(amount)
                    medicine.display()
                    break


    elif choice == "4":

        medicine_id = get_medicine_id()

        amount = int(input("How many medicine to sell: "))

        if amount <= 0:

            print("Invalid Amount")

        else:

            for medicine in inventory:

                if medicine.Medicine_ID == medicine_id:

                    if amount > medicine.Quantity:

                        print("Not enough stock")

                    else:

                        medicine.sell_stock(amount)
                        medicine.display()

                    break


    elif choice == "5":

        medicine_id = get_medicine_id()

        delete_medicine(inventory, medicine_id)


    elif choice == "6":

        medicine_id = get_medicine_id()

        update_medicine(inventory, medicine_id)


    elif choice == "7":

        expiry_medicine(inventory)


    elif choice == "8":

        check_low_stock(inventory)


    elif choice == "9":

        print("Exiting Medicine Inventory Tracker...")
        break