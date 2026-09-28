correct_pin = "4521"

while True:
    pin = input("Enter PIN: ")

    if pin == "cancel":
        print("Transaction Cancelled.")
        break

    if pin == correct_pin:
        print("Access Granted!")
        break
    else:
        print("Incorrect PIN, try again.")






