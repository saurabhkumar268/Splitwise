friends = {} 
history = []  

print("---  Advanced Splitwise Setup ---")


print("Enter friend names. Type 'done' when finished.")
while True:
    name = input("Enter name: ").strip().title()
    if name == 'Done':
        break

    if name in friends:
        print("Name already exists.")
    else:
        friends[name] = 0.0
        print(f"Added {name}.")

running = True


while running:

    total_people = len(friends)
    
    print("\n" + "="*30)
    print("       MENU OPTIONS       ")
    print("="*30)
    print("1. Add an Expense")
    print("2. View Balances (Who owes what)")
    print("3. View Transaction History") 
    print("4. Add a New Friend")         
    print("5. Exit")
    
    choice = input("\nEnter choice (1-5): ")


    if choice == '1':
        if total_people == 0:
            print("Error: No friends in the group yet.")
            continue

        print("\n---  Add Expense ---")
        payer = input("Who paid the bill? ").strip().title()

        if payer in friends:
            try:
                item = input("What was this for? (e.g. Pizza): ").title() # NEW
                amount = float(input(f"How much did {payer} pay? "))

              
                friends[payer] = friends[payer] + amount
                
              
                split_amount = amount / total_people

               
                for name in friends:
                    friends[name] = friends[name] - split_amount

                record = f"{payer} paid {amount} for {item}. (Each person owes {round(split_amount, 2)})"
                history.append(record)

                print(f" Added! Everyone's share is: {round(split_amount, 2)}")
                
            except ValueError:
                print(" Error: Please enter a valid number for amount.")
        else:
            print(f" Error: {payer} is not in the group list.")

 
    elif choice == '2':
        print("\n---  Current Balances ---")
        print("(Positive = Get Money | Negative = Pay Money)")
        print("-" * 45)

        for name, balance in friends.items():
            final_val = round(balance, 2)
            
            if final_val > 0:
                print(f" {name} gets back: {final_val}")
            elif final_val < 0:
                print(f" {name} needs to pay: {abs(final_val)}")
            else:
                print(f" {name} is settled (0.0)")


    elif choice == '3':
        print("\n---  Transaction History ---")
        if not history:
            print("No transactions yet.")
        else:

            for i, record in enumerate(history):
                print(f"{i+1}. {record}")

    elif choice == '4':
        new_friend = input("Enter new friend's name: ").strip().title()
        
        if new_friend in friends:
            print("That person is already in the group.")
        else:
          
            friends[new_friend] = 0.0
            print(f" {new_friend} has been added to the group!")
            print("Note: They will only split future bills, not past ones.")

    elif choice == '5':
        print("Exiting Splitwise... Goodbye!")
        running = False

    else:
        print("Invalid choice.")
