import random

# Function to generate a random 10-digit lottery ticket number
def generate_lottery_ticket():
    return random.randint(1000000000, 9999999999)

# Generate 100 unique random lottery tickets
lottery_tickets = set()
while len(lottery_tickets) < 100:
    ticket_number = generate_lottery_ticket()
    lottery_tickets.add(ticket_number)

# Select two lucky tickets as winners
winners = random.sample(lottery_tickets, 2)

print("List of 100 unique random lottery tickets:")
print(lottery_tickets)
print("\nTwo lucky winners:")
print(winners)
