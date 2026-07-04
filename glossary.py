import csv

print("Welcome To Glossary!!!".center(100))

d1 = {}

def add_word():
    word = input("Add word : ").lower()

    with open("glossary.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["WORD"] == word:
                print(f"'{word}' already exists with meaning: {row['MEANING']}")
                return
    
    meaning = input("Add meaning : ")
    d1[word] = meaning


    with open("glossary.csv", "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["WORD", "MEANING"])
        writer.writerow({"WORD": word, "MEANING": meaning})
        print(f"Added '{word}' to glossary.")

def find_meaning():
    word = input("Enter word to find meaning : ").lower()
    with open("glossary.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["WORD"] == word:
                print(f"{row['WORD']} : {row['MEANING']}")
                return
    print("Word not found in glossary!")

def list_all():
    with open("glossary.csv", "r", newline="") as f:
        list1=[]
        reader = csv.DictReader(f)
        print()
        print("Glossary Words".center(100))
        for row in reader:
            list1.append([row['WORD'],row['MEANING']])
        for item in sorted(list1):
            word = item[0]
            meaning = item[1]
            print(f"\n{word.upper()} : {meaning.capitalize()}")

while True:
    a = int(input("\nEnter 1 to add word in glossary , 2 for knowing words meaning , 3 to list all word , 4 to exit : "))
    match a:
        case 1:
            add_word()
        case 2:
            find_meaning()
        case 3:
            list_all()
        case 4:
            break