# Overview

As a software engineer, my goal is to further develop my skills in working with databases and creating practical, real-world applications. For this project, I created an Inventory Management System that integrates with a SQL Relational Database using SQLite. The system allows users to add, update, delete, and view items in the inventory, keeping track of essential details like item name, quantity, price, and description.

This software is a command-line application where users can input commands to interact with the inventory. Behind the scenes, SQL queries are executed to perform the corresponding operations (e.g., INSERT, UPDATE, DELETE, SELECT) on the SQLite database. The program provides a simple interface for inventory management and allows users to interact with the database without needing to write SQL themselves.

[Software Demo Video](https://vimeo.com/1030414407?share=copy#t=0)

# Relational Database

## Database Structure:
The database consists of a single table, inventory, which includes the following columns:

- item_id (INTEGER, Primary Key, Auto Increment): A unique identifier for each inventory item.
- name (TEXT): The name of the item.
- quantity (INTEGER): The number of units of the item available in the inventory.
- price (REAL): The price of each unit of the item.
- description (TEXT): A textual description of the item.
This structure allows easy storage and retrieval of inventory items, and supports the basic CRUD operations needed for inventory management.

# Development Environment

## Tools Used:
Python: The programming language used to write the application.
SQLite: The relational database management system used to store inventory data. It is accessed via Python’s built-in sqlite3 library.
Text Editor/IDE: I used Visual Studio Code to write the Python code for the project.

## Libraries:
sqlite3: A standard Python library used to interact with SQLite databases. It enables creating tables, inserting data, updating records, and performing queries.

# Useful Websites

- [SQLite3](https://docs.python.org/3/library/sqlite3.html)
- [Python](https://www.python.org/)

# Future Work

- Error Handling: Implement more robust error handling to ensure the program can handle invalid inputs gracefully.
- Search Functionality: Add a search feature that allows users to search for items based on name, price, or other attributes.
- Graphical User Interface (GUI): Develop a simple GUI for the program using a Python library like Tkinter or PyQt, making it more user-friendly.