import random

# Slot symbols
symbols = ["🍒", "🍋", "🔔", "🍉", "⭐", "7️⃣"]

# Payout table based on matched symbols
payout_table = {
    "🍒": 10,
    "🍋": 20,
    "🔔": 30,
    "🍉": 40,
    "⭐": 50,
    "7️⃣": 100
}

def spin_slots():
    return [random.choice(symbols) for _ in range(3)]

def check_win(slots):
    if slots[0] == slots[1] == slots[2]:
        return payout_table[slots[0]]
    elif slots[0] == slots[1] or slots[1] == slots[2] or slots[0] == slots[2]:
        return 5  # Small reward for partial match
    else:
        return 0

def play():
    balance = 100
    print("🎰 Welcome to the Python Slot Machine!")
    print("You start with $100. Each spin costs $10.")

    while balance >= 10:
        input("\nPress Enter to spin...")
        balance -= 10
        slots = spin_slots()
        print(" | ".join(slots))

        winnings = check_win(slots)
        if winnings > 0:
            print(f"🎉 You won ${winnings}!")
            balance += winnings
        else:
            print("😞 No win this time.")

        print(f"Current balance: ${balance}")

        if balance < 10:
            print("\n💸 You're out of money. Game over!")
            break

        play_again = input("Do you want to spin again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play()
