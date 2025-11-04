import csv
import datetime
import random as r
FILE_NAME = r"C:\Users\abhij\OneDrive - MSFT\Documents\Mine\Abhijeeth's\2025 VIT college work\SEM1\Problem Solving Using Python\Python project credited\atm_users.csv"


#Register
def register():
    username = input("Enter a new username: ").strip()
    pin = input("Enter a 4-digit PIN: ").strip()

    if not pin.isdigit() or len(pin) != 4:
        print("❌ PIN must be exactly 4 digits.")
        return

    #Check if user exists
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            if row[0] == username:
                print("❌ Username already exists. Try again.")
                return
            
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, pin, 0.0, 0.0, 0.0, 0.0, 0.0])
    print("✅ Registration successful! You can now log in.")

#Login
def login():
    username = input("Enter username: ").strip()
    pin = input("Enter your 4-digit PIN: ").strip()

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            if row[0] == username and row[1] == pin:
                print(f"\n✅ Login successful! Welcome, {username}.")
                atm_menu(username)
                return
    print("❌ Invalid username or PIN.")

#Services
def list_services(username):
    print(""" 1. Bill Payments
    2. Mobile Recharge
    3. Funds Transfer""")

    ch = int(input("Enter choice: "))

    if ch == 1:
        rows = []
        user_data = None

        # Read user data
        with open(FILE_NAME, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
                if row["Username"] == username:
                    user_data = row

        if not user_data:
            print("❌ User not found!")
            return

        print("""1. Electricity Bill
2. Water Bill
3. Gas Bill
4. Loan Payment""")
        ch2 = int(input("Enter choice: "))
        # --- ELECTRICITY BILL ---
        if ch2 == 1:
            print(f"💡 Electricity bill amount: ₹{user_data['ElectricityBill']}")
            amount = float(input("Enter amount to pay: ₹"))
            balance = float(user_data["Balance"])
            bill_amount = float(user_data["ElectricityBill"])

            if amount > balance:
                print("❌ Insufficient balance.")
                return
            if amount > bill_amount:
                print("❌ You cannot pay more than the bill amount.")
                return

            user_data["Balance"] = str(balance - amount)
            user_data["ElectricityBill"] = str(bill_amount - amount)
            print("✅ Electricity Bill paid successfully!")

        # --- WATER BILL ---
        elif ch2 == 2:
            print(f"🚿 Water bill amount: ₹{user_data['WaterBill']}")
            amount = float(input("Enter amount to pay: ₹"))
            balance = float(user_data["Balance"])
            bill_amount = float(user_data["WaterBill"])

            if amount > balance:
                print("❌ Insufficient balance.")
                return
            if amount > bill_amount:
                print("❌ You cannot pay more than the bill amount.")
                return

            user_data["Balance"] = str(balance - amount)
            user_data["WaterBill"] = str(bill_amount - amount)
            print("✅ Water Bill paid successfully!")

        # --- GAS BILL ---
        elif ch2 == 3:
            print(f"🔥 Gas bill amount: ₹{user_data['GasBill']}")
            amount = float(input("Enter amount to pay: ₹"))
            balance = float(user_data["Balance"])
            bill_amount = float(user_data["GasBill"])

            if amount > balance:
                print("❌ Insufficient balance.")
                return
            if amount > bill_amount:
                print("❌ You cannot pay more than the bill amount.")
                return

            user_data["Balance"] = str(balance - amount)
            user_data["GasBill"] = str(bill_amount - amount)
            print("✅ Gas Bill paid successfully!")

        # --- LOAN PAYMENT ---
        elif ch2 == 4:
            print(f"💰 Loan amount pending: ₹{user_data['Loan']}")
            amount = float(input("Enter amount to pay: ₹"))
            balance = float(user_data["Balance"])
            bill_amount = float(user_data["Loan"])

            if amount > balance:
                print("❌ Insufficient balance.")
                return
            if amount > bill_amount:
                print("❌ You cannot pay more than the loan amount.")
                return

            user_data["Balance"] = str(balance - amount)
            user_data["Loan"] = str(bill_amount - amount)
            print("✅ Loan payment recorded successfully!")

        else:
            print("❌ Invalid option.")
            return

        # --- Save back to file ---
        with open(FILE_NAME, "w", newline="") as f:
            fieldnames = ["Username", "PIN", "Balance", "ElectricityBill", "WaterBill", "GasBill", "Loan"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print(f"💰 Remaining Balance: ₹{user_data['Balance']}")
        if ch2 == 1:
            print(f"📉 Outstanding Electricity Bill: ₹{user_data['ElectricityBill']}")
        elif ch2 == 2:
            print(f"📉 Outstanding Water Bill: ₹{user_data['WaterBill']}")
        elif ch2 == 3:
            print(f"📉 Outstanding Gas Bill: ₹{user_data['GasBill']}")
        elif ch2 == 4:
            print(f"📉 Outstanding Loan Amount: ₹{user_data['Loan']}")
    elif ch == 2:
        with open(FILE_NAME, 'r', newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)

        mbno = input("Enter mobile number to recharge: ").strip()
        amount = float(input("Enter recharge amount: ₹"))

        if not (mbno.isdigit() and len(mbno) == 10):
            print("❌ Invalid phone number. Must be 10 digits.")
        else:
            updated = False
            for i in rows:
                if i[0] == username:
                    balance = float(i[2])
                    if balance >= amount:
                        balance -= amount
                        i[2] = str(balance)
                        updated = True
                        print(f"✅ Recharge of ₹{amount:.2f} to {mbno} successful!")
                    break

            if updated:
                with open(FILE_NAME, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(rows)


    elif ch == 3:  
        receiver = input("Enter receiver's username: ").strip()
        amount = float(input("Enter amount to transfer: ₹"))

        if amount <= 0:
            print("❌ Invalid amount.")
            return  # ✅ must stay inside this block

        sender_balance = get_balance(username)
        if amount > sender_balance:
            print("❌ Insufficient balance for transfer.")
            return

        rows = []
        sender_found = False
        receiver_found = False

        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                if row[0] == username:
                    row[2] = str(float(row[2]) - amount)
                    sender_found = True
                elif row[0] == receiver:
                    row[2] = str(float(row[2]) + amount)
                    receiver_found = True
                rows.append(row)

        if not receiver_found:
            print("❌ Receiver username not found. Transfer cancelled.")
            return

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)

        print(f"✅ ₹{amount:.2f} transferred successfully to {receiver}.")


#Pin change
def change_pin(username):
    old_pin = input("Enter your current PIN: ").strip()
    new_pin = input("Enter your new 4-digit PIN: ").strip()

    if not new_pin.isdigit() or len(new_pin) != 4:
        print("❌ New PIN must be exactly 4 digits.")
        return

    
    rows = []
    pin_changed = False
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row[0] == username:
                if row[1] == old_pin:
                    row[1] = new_pin
                    pin_changed = True
                else:
                    print("❌ Incorrect current PIN.")
                    return
            rows.append(row)

    if pin_changed:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)
        print("✅ PIN changed successfully!")
    else:
        print("❌ User not found.")


#ATM Menu
def atm_menu(username):
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Services")
        print("5. Change PIN")
        print("6. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            balance = get_balance(username)
            print(f"💰 Current Balance: ₹{balance:.2f}")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹"))
            update_balance(username, amount)
            print(f"✅ ₹{amount:.2f} deposited successfully.")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))
            withdraw(username, amount)
        
        elif choice == "4":
            list_services(username)


        elif choice == "5":
            change_pin(username)

        elif choice == "6":
            print("👋 Logged out successfully.\n")
            break
        
    
        else:
            print("❌ Invalid choice. Try again.")

#Get Balance
def get_balance(username):
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0] == username:
                return float(row[2])
    return 0.0

#Deposit / Update
def update_balance(username, amount):
    rows = []
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row[0] == username:
                row[2] = str(float(row[2]) + amount)
            rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

#Withdraw
def withdraw(username, amount):
    rows = []   
    success = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row[0] == username:
                balance = float(row[2])
                if amount <= balance:
                    row[2] = str(balance - amount)
                    success = True
                    print(f"✅ ₹{amount:.2f} withdrawn successfully.")
                else:
                    print("❌ Insufficient balance.")
            rows.append(row)

    if success:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)
        
        choice = input("Do you want a printed receipt? (y/n): ").strip().lower()
        if choice == "y":
            print("\n" + "="*30)
            print("           🏧 ATM RECEIPT")
            print("="*30)
            print(f"Username: {username}")
            print(f"Amount Withdrawn: ₹{amount:.2f}")
            print(f"Remaining Balance: ₹{balance-amount:.2f}")
            print(f"Date & Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("="*30)
            print("Thank you for using our ATM!")
            print("="*30 + "\n")
            
