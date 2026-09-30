````markdown
# 🔭 Antariksh Science Glossary

A simple command-line glossary built to store and manage technical and scientific terms encountered while reading research papers.

## 📌 Why This Project?

While reading research papers, scientific terms often have meanings that are more specific than their general definitions found online.

This project was created for the **Antariksh Science Department** to keep a personal collection of technical terms and their research-specific meanings in one place.

Instead of repeatedly searching for the same terminology, terms can be added, searched, and reviewed directly from the terminal.

## ✨ Features

- ➕ Add new scientific or technical terms
- 🔎 Search for the meaning of a term
- 📚 Display all stored glossary terms
- 🔤 Automatically sort terms alphabetically
- 🚫 Prevent duplicate terms from being added
- 💾 Store glossary data permanently in a CSV file
- 💻 Simple command-line interface

## 🛠️ Tech Stack

- **Language:** Python
- **Data Storage:** CSV

## 📂 Project Structure

```text
antariksh_science_glossary/
│
├── glossary.py
├── glossary.csv
├── .gitignore
└── README.md
````

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/aaditya-hamirani07/antariksh_science_glossary.git
```

### 2. Navigate to the Project

```bash
cd antariksh_science_glossary
```

### 3. Run the Program

```bash
python glossary.py
```

## 🖥️ How It Works

After running the program, you get a menu with four options:

```text
Enter 1 to add word in glossary
2 for knowing words meaning
3 to list all word
4 to exit
```

### 1️⃣ Add a Word

Enter a scientific or technical term and its meaning.

```text
Add word : spectroscopy
Add meaning : The study of how matter interacts with electromagnetic radiation.

Added 'spectroscopy' to glossary.
```

If the term already exists, the program displays its stored meaning instead of adding a duplicate.

### 2️⃣ Find a Meaning

Search for a previously stored term.

```text
Enter word to find meaning : spectroscopy

spectroscopy : The study of how matter interacts with electromagnetic radiation.
```

### 3️⃣ List All Terms

Displays all stored terms and their meanings in alphabetical order.

```text
GLOSSARY WORDS

EXOPLANET : A planet that exists outside our solar system.

SPECTROSCOPY : The study of how matter interacts with electromagnetic radiation.
```

### 4️⃣ Exit

Closes the glossary program.

## 💾 Data Storage

Glossary entries are stored in `glossary.csv`.

The CSV follows this structure:

```text
WORD,MEANING
```

Example:

```text
Exoplanet,A planet outside our solar system
Spectroscopy,Study of interaction between matter and electromagnetic radiation
```

This allows the glossary to retain terms even after the program is closed.

## 🧠 Concepts Used

This project was built using basic Python concepts including:

* Functions
* Dictionaries
* Loops
* Conditional statements
* Pattern matching with `match`
* File handling
* CSV processing
* User input
* Sorting
* String manipulation

## 🎯 Use Case

This project is particularly useful for:

* 📄 Research paper reading
* 🔭 Astronomy and space science terminology
* 🧪 Scientific terminology
* 📚 Personal study notes
* 📝 Maintaining a research vocabulary

The glossary can also be expanded over time as new research papers introduce unfamiliar terminology.