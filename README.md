# 🔭 Antariksh Science Glossary

A simple command-line Python glossary for storing and searching scientific and technical terms encountered while reading research papers.

## ✨ Features

- ➕ Add new scientific or technical terms
- 🔎 Search for the meaning of a term
- 📚 Display all glossary terms
- 🔤 Sort terms alphabetically
- 🚫 Avoid duplicate entries
- 💾 Store entries permanently in a CSV file
- 💻 Simple command-line interface

## 🛠️ Tech Stack

- **Language:** Python
- **Module:** `csv`
- **Storage:** CSV

## 📂 Project Structure

```text
antariksh_science_glossary/
│
├── glossary.py
├── glossary.csv
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/aaditya-hamirani07/antariksh_science_glossary.git
```

### Open the project

```bash
cd antariksh_science_glossary
```

### Run the program

```bash
python glossary.py
```

## 🖥️ Usage

When the program starts, you can choose from the available options:

```text
1. Add word in glossary
2. Find word meaning
3. List all words
4. Exit
```

### Add a Word

Enter a scientific term and its meaning. The term is saved to the glossary CSV file.

### Find a Meaning

Enter a stored term to retrieve its meaning.

### List All Words

Displays the terms currently stored in the glossary in alphabetical order.

### Exit

Closes the program.

## 💾 Data Storage

All glossary entries are stored in `glossary.csv`.

Example:

```csv
WORD,MEANING
Exoplanet,A planet outside our solar system
Spectroscopy,The study of how matter interacts with electromagnetic radiation
```

Because the data is stored in a CSV file, entries remain available when the program is run again.

## 🧠 Concepts Used

This project uses basic Python concepts such as:

- Functions
- Dictionaries
- Loops
- Conditional statements
- Pattern matching
- File handling
- CSV processing
- User input
- Sorting
- String manipulation

## 🎯 Purpose

The glossary was created for maintaining scientific terminology encountered during research-paper reading, particularly in areas related to **space science, astronomy, and scientific research**.

It provides a quick way to record unfamiliar terms and refer back to their meanings later.

## 🔮 Future Improvements

- [ ] Add categories for different scientific fields
- [ ] Add edit and delete functionality
- [ ] Add case-insensitive search
- [ ] Add partial-word search
- [ ] Add examples for each term
- [ ] Add timestamps
- [ ] Add a GUI
- [ ] Convert it into a web-based glossary

## 👨‍💻 Author

**Aaditya Hamirani**

B.Tech Artificial Intelligence & Machine Learning  
Dwarkadas J. Sanghvi College of Engineering

GitHub: https://github.com/aaditya-hamirani07

## 📄 License

This project is intended for learning, experimentation, and further development.
