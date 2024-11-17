import sqlite3

# Function to connect to the SQLite database
def connect_db():
    return sqlite3.connect('inventory.db')

# Function to create the inventory table
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory (
                        item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        quantity INTEGER NOT NULL,
                        price REAL NOT NULL,
                        description TEXT)''')
    conn.commit()
    conn.close()

# Function to add a new item to the inventory
def add_item(name, quantity, price, description):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO inventory (name, quantity, price, description)
                      VALUES (?, ?, ?, ?)''', (name, quantity, price, description))
    conn.commit()
    conn.close()
    print("Item added successfully.")

# Function to update an existing item in the inventory
def update_item(item_id, name, quantity, price, description):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''UPDATE inventory
                      SET name = ?, quantity = ?, price = ?, description = ?
                      WHERE item_id = ?''', (name, quantity, price, description, item_id))
    conn.commit()
    conn.close()
    print("Item updated successfully.")

# Function to delete an item from the inventory
def delete_item(item_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM inventory WHERE item_id = ?''', (item_id,))
    conn.commit()
    conn.close()
    print("Item deleted successfully.")

# Function to view all items in the inventory
def view_inventory():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM inventory''')
    rows = cursor.fetchall()
    if rows:
        print("Inventory List:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Quantity: {row[2]}, Price: ${row[3]}, Description: {row[4]}")
    else:
        print("No items in the inventory.")
    conn.close()

# Main function to run the command-line interface
def main():
    create_table()
    
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Delete Item")
        print("4. View Inventory")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            description = input("Enter item description: ")
            add_item(name, quantity, price, description)

        elif choice == '2':
            item_id = int(input("Enter item ID to update: "))
            name = input("Enter new item name: ")
            quantity = int(input("Enter new item quantity: "))
            price = float(input("Enter new item price: "))
            description = input("Enter new item description: ")
            update_item(item_id, name, quantity, price, description)

        elif choice == '3':
            item_id = int(input("Enter item ID to delete: "))
            delete_item(item_id)

        elif choice == '4':
            view_inventory()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid option, please choose again.")

if __name__ == '__main__':
    main()