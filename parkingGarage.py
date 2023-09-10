class ParkingGarage:
    def __init__(self, max_spaces):
        self.max_spaces = max_spaces
        self.available_spaces = max_spaces
        self.tickets = {}
        
    def take_ticket(self):
        if self.available_spaces > 0:
            ticket_number = len(self.tickets) + 1
            self.tickets[ticket_number] = {"paid": False}
            self.available_spaces -= 1
            print(f"Ticket #{ticket_number} issued. {self.available_spaces} parking spaces left.")
        else:
            print("Sorry, the garage is full.")
    
    def pay_for_parking(self, ticket_number):
        if ticket_number in self.tickets:
            if not self.tickets[ticket_number]["paid"]:
                amount = input("Enter the amount to pay for parking: $")
                if amount:
                    self.tickets[ticket_number]["paid"] = True
                    print(f"Ticket #{ticket_number} has been paid. You have 10 minutes to leave.")
                else:
                    print("Payment not received.")
            else:
                print(f"Ticket #{ticket_number} has already been paid.")
        else:
            print(f"Invalid ticket number: #{ticket_number}")
    
    def leave_garage(self, ticket_number):
        if ticket_number in self.tickets:
            if self.tickets[ticket_number]["paid"]:
                del self.tickets[ticket_number]
                self.available_spaces += 1
                print("Thank you, have a nice day!")
            else:
                print("Please pay for parking before leaving.")
        else:
            print(f"Invalid ticket number: #{ticket_number}")


if __name__ == "__main__":
    garage = ParkingGarage(200)
    
    while True:
        print("\nOptions:")
        print("1. Take a ticket")
        print("2. Pay for parking")
        print("3. Leave the garage")
        print("4. Exit")
        choice = input("Select an option (1/2/3/4): ")

        if choice == "1":
            garage.take_ticket()
        elif choice == "2":
            ticket_number = int(input("Enter your ticket number: "))
            garage.pay_for_parking(ticket_number)
        elif choice == "3":
            ticket_number = int(input("Enter your ticket number: "))
            garage.leave_garage(ticket_number)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")
