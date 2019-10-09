import sqlite3

db = sqlite3.connect("files/my_base.db")


def create_table():
    db.row_factory = sqlite3.Row
    db.execute("create table if not exists People(ID integer primary key autoincrement, Name text, Age int)")
    db.commit()


def add_record(Name, Age):
    db.row_factory = sqlite3.Row
    db.execute("INSERT INTO People(Name, Age) values(?, ?)", (Name, Age))
    db.commit()
    print("Record is added")


def list_people():
    listy = db.execute("SELECT * FROM People")
    print("\n")
    for row in listy:
        print("ID:{}\t Name: {}\t Age: {}".format(row["ID"], row["Name"], row["Age"]))


def delete_record(id):
    db.row_factory = sqlite3.Row
    db.execute("DELETE FROM People WHERE ID='{}'".format(id))
    db.commit()
    print("Record is deleted")


def update_record(id, age):
    db.row_factory = sqlite3.Row
    db.execute("UPDATE People SET Age=? WHERE ID=?", (age, id))
    db.commit()
    print("Record is Updated")


def main():
    create_table()
    while 1:
        index_num = int(input("\n===\nSelect Operation:\n"
                              "1 - Add.\n2 - Update age.\n3 - Delete.\n"
                              "4 - List people.\n0 - Exit\n"))
        if(index_num == 0):
            break
        elif(index_num == 1):
            name = input("Enter name:\t")
            age = int(input("Enter Age:\t"))
            add_record(name, age)
        elif(index_num == 2):
            id = int(input("Enter person ID:\t"))
            age = int(input("Enter new Age:\t"))
            update_record(id, age)
        elif(index_num == 3):
            id = int(input("Enter ID to delete:\t"))
            delete_record(id)
        elif(index_num == 4):
            list_people()


if __name__ == "__main__":
    main()
