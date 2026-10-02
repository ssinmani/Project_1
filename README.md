# Medicine Inventory Tracker

A simple command-line program written in Python for managing a pharmacy's medicine inventory. It loads medicine records from a JSON file and lets you view, search, restock, sell, update, and delete medicines, as well as check for expired or low-stock items.

## Features

- **Display medicines**: list every medicine with its full details
- **Search medicine**: look up a medicine by its ID
- **Add stock**: increase the quantity of a medicine
- **Sell medicine**: reduce the quantity, with a check to prevent selling more than is available
- **Delete medicine**: remove a medicine from the inventory
- **Update medicine**: change a medicine's price
- **Check expiry**: report which medicines are expired based on today's date
- **Check low stock**: flag medicines with a quantity below 30

## Requirements

- Python 3.6 or later
- No external libraries (uses only the built-in `json` and `datetime` modules)

## Project Structure

```
.
├── main.py           # The inventory tracker program
├── inventory.json    # Medicine data loaded at startup
└── README.md
```

## Inventory File Format

The program expects a file named `inventory.json` in the same directory it is run from. The file should contain a list of medicine objects with these fields:

| Field           | Type    | Description                              |
|-----------------|---------|------------------------------------------|
| `Medicine_ID`   | integer | Unique identifier for the medicine       |
| `Medicine_name` | string  | Name of the medicine                     |
| `Category`      | string  | Category (e.g. Painkiller, Antibiotic)   |
| `Quantity`      | integer | Number of units in stock                 |
| `Price`         | number  | Price per unit                           |
| `Expiry_date`   | string  | Expiry date in `MM/DD/YYYY` format       |

### Example `inventory.json`

```json
[
  {
    "Medicine_ID": 101,
    "Medicine_name": "Paracetamol",
    "Category": "Painkiller",
    "Quantity": 120,
    "Price": 2.5,
    "Expiry_date": "12/31/2027"
  },
  {
    "Medicine_ID": 102,
    "Medicine_name": "Amoxicillin",
    "Category": "Antibiotic",
    "Quantity": 25,
    "Price": 8.0,
    "Expiry_date": "03/15/2026"
  }
]
```

> **Note:** `Medicine_ID` must be stored as a number, not a string, because the program compares it against an integer entered by the user.

## How to Run

1. Place `main.py` and `inventory.json` in the same folder.
2. Open a terminal in that folder.
3. Run:

```bash
python main.py
```

## Usage

When the program starts, it shows this menu:

```
1. Display medicines
2. Search medicine
3. Add stock
4. Sell medicine
5. Delete medicine
6. Update medicine
7. Check expiry
8. Check low stock
9. Exit
Enter your choice:
```

Type a number and press Enter. Options that act on a single medicine will ask for a medicine ID first.

### Example session

```
Enter your choice: 4
Enter the medicine Id:101
How many medicine to sell: 20
Medicine ID: 101
Medicine_name: Paracetamol
Category: Painkiller
Quantity: 100
Price: 2.5
Expiry: 12/31/2027
```

## Code Overview

| Component              | Purpose                                                        |
|------------------------|----------------------------------------------------------------|
| `load_inventory()`     | Reads `inventory.json` and returns the raw data                |
| `Medicine` class       | Represents one medicine; includes `display`, `add_stock`, `sell_stock`, `check_low_stock` |
| `create_inventory()`   | Converts the JSON data into a list of `Medicine` objects       |
| `get_medicine_id()`    | Prompts the user for a medicine ID                             |
| `search_medicine()`    | Finds and prints a medicine by ID                              |
| `delete_medicine()`    | Removes a medicine by ID                                       |
| `update_medicine()`    | Updates a medicine's price                                     |
| `expiry_medicine()`    | Compares each expiry date with today's date                    |
| `check_low_stock()`    | Flags medicines with quantity below 30                         |
| `menu()`               | Displays the menu and returns the user's choice                |

## Known Limitations

- **Changes are not saved.** All edits happen in memory only; `inventory.json` is not updated, so changes are lost when the program exits.
- **Update sets a fixed price.** Option 6 always sets the price to `6` instead of asking the user for a new price.
- **No input validation for non-numbers.** Entering letters where a number is expected (ID or amount) will crash the program with a `ValueError`.
- **Missing IDs give no feedback** in Add stock, Sell, Delete, and Update; nothing happens if the ID doesn't exist.
- **Invalid menu choices are silently ignored.**

## Possible Improvements

- Save changes back to `inventory.json` after each edit or on exit
- Let the user enter the new price (and other fields) when updating
- Add an option to create new medicine records
- Wrap numeric input in `try/except` to handle invalid entries gracefully
- Show "Medicine not found" messages for unknown IDs
- Make the low-stock threshold configurable
