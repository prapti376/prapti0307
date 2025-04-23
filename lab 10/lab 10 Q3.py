name = input("Enter your name: ")
phone = input("Enter your phone number: ")
email = input("Enter your email address: ")
address = input("Enter your address: ")

contact_card = [name + "\n", phone + "\n", email + "\n", address + "\n"]

with open(r"C:\Users\Prapti\Desktop\contact_card.txt", "w") as file:
    file.writelines(contact_card)