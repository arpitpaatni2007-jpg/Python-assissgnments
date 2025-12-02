# 📚 Library Inventory Manager  
### A Mini Project for Python – OOP, JSON, File Handling & CLI

This project is a simple and efficient **Library Inventory Management System** built using Python.  
It demonstrates important programming concepts such as:

- Object-Oriented Programming (OOP)
- File handling using JSON
- Exception handling
- Logging
- Modular programming
- Command Line Interface (CLI)

This project was developed as part of a university lab/assignment.

---

## 🚀 Features

### 🔹 Book Management  
- Add new books  
- Issue a book  
- Return a book  
- Check availability  

### 🔹 Search & Display  
- Search by title  
- Search by ISBN  
- View complete inventory  

### 🔹 Data Persistence  
- Books are saved in a JSON file (`catalog.json`)  
- Automatically loads data when program starts  

### 🔹 Logging  
- All actions are logged in `library.log`  
- Helpful for debugging and tracking usage  

### 🔹 Modular Structure  
- `book.py` → Contains the **Book** class  
- `inventory.py` → Contains the **LibraryInventory** class  
- `main.py` → Command-line user interface  

---

## 📁 Project Structure

library-inventory-manager/
│
├── book.py # Book class (title, author, isbn, status)
├── inventory.py # Inventory manager + JSON handling
├── main.py # CLI menu interface
│
├── catalog.json # Auto-created JSON database
├── library.log # Log file (optional)
│
├── README.md # Project documentation
├── requirements.txt # Dependencies


---

## 🛠️ How to Run the Project

### 1. Install Python 3  
Make sure Python is installed.

### 2. Clone the repository 

git clone https://github.com/arpitpaatni2007-jpg/Assissgnment-3.git

### 3. Open the folder  
cd library-inventory-manager

graphql
Copy code

### 4. Run the CLI  
python main.py

yaml
Copy code

You will see:

========== Library Inventory Manager ==========

Add Book

Issue Book

Return Book

View All Books

Search Book

Exit
===============================================
Enter your choice:

yaml
Copy code

---

## 📝 Example Usage

**Add a Book →**  
Enter:
1
Harry Potter
J.K. Rowling
1111

css
Copy code

**Issue a Book →**  
2
1111

css
Copy code

**Return a Book →**  
3
1111

sql
Copy code

**View All Books →**  
4

yaml
Copy code

---

## 📦 JSON Database (catalog.json)

Example content:
```json
[
  {
    "title": "Harry Potter",
    "author": "J.K. Rowling",
    "isbn": "1111",
    "status": "available"
  }
]
# 🧪 Requirements
json
pathlib
logging

# 👨‍💻 Author

Arpit
Library Inventory Mini Project – Python Assignment




