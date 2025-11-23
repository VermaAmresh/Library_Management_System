import json
from datetime import datetime


LIB_DB = "books.json"


def load_data():
    try:
        with open(LIB_DB, "r") as fobj:
            info = json.load(fobj)
            return info
    except:
        return []  



def save_data(records):
    with open(LIB_DB, "w") as fp:
        json.dump(records, fp, indent=4)



def add_book():
    data = load_data()

  
    b_id = input("Book ID daaliye: ").strip()
    name_book = input("Book ka title: ").strip()
    writer = input("Author ka naam: ").strip()

    temp = {
        "id": b_id,
        "title": name_book,
        "author": writer,
        "issued": False,
        "issuer": "",
        "issue_date": ""
    }

    data.append(temp)
    save_data(data)
    print("Book list me add ho gayi.\n")



def display_books():
    stuff = load_data()

    if len(stuff) == 0:
        print("Library me abhi koi book nahi hai.\n")
        return

   
    for b in stuff:
        print("\nID :", b.get("id"))
        print("Title :", b.get("title"))
        print("Author :", b.get("author"))
        print("Issued :", b.get("issued"))

        if b.get("issued"):
            print("Issued To :", b.get("issuer"))
            print("Issued On :", b.get("issue_date"))

        print("-" * 40)



def issue_book():
    books = load_data()
    book_key = input("Kis book ka ID chahiye (issue): ").strip()

    found = False
    for entry in books:
        if entry.get("id") == book_key:
            found = True

            if entry.get("issued"):
                print("Ye book pehle hi kisi ke paas hai.\n")
                return

            person = input("Iss book ko kaun le raha hai? ").strip()

            entry["issued"] = True
            entry["issuer"] = person
            entry["issue_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            save_data(books)
            print("Book issue ho gayi.\n")
            return

    if not found:
        print("Book ID galat hai.\n")



def return_book():
    items = load_data()
    key = input("Return ke liye book ID daaliye: ").strip()

    chk = False
    for it in items:
        if it["id"] == key:
            chk = True

            if not it["issued"]:
                print("Ye book issue hi nahi thi.\n")
                return

           
            d1 = datetime.strptime(it["issue_date"], "%Y-%m-%d %H:%M:%S")
            d2 = datetime.now()

            total_days = (d2 - d1).days
            pending = total_days - 7
            amount = 0

            if pending > 0:
                amount = pending * 50

           
            it["issued"] = False
            it["issuer"] = ""
            it["issue_date"] = ""

            save_data(items)

            print("Book return ho gayi.")
            print("Kitne din rakhi:", total_days)
            print("Fine:", amount, "/-\n")
            return

    if not chk:
        print("Book nahi mili.\n")