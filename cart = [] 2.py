candidates = ["Alice", "Bob", "Charlie"]
voters = []
votes = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0
}
def show_candidates():
    print("\n--- Candidates ---")
    for candidate in candidates:
        print("-", candidate)
def vote():
    name = input("Enter your name: ").strip()
    if name in voters:
        print("❌ You have already voted!")
        return
    print("\nChoose a candidate:")
    for candidate in candidates:
        print("-", candidate)
    choice = input("Your choice: ").strip()
    if choice not in candidates:
        print("❌ Invalid candidate!")
        return
    votes[choice] += 1
    voters.append(name)
    print("✅ Vote recorded.")
def show_results():
    print("\n--- Results ---")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} votes")
def main():
    while True:
        print("\n===== Voting System =====")
        print("1. Show candidates")
        print("2. Vote")
        print("3. Show results")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            show_candidates()
        elif choice == "2":
            vote()
        elif choice == "3":
            show_results()
        elif choice == "4":
            print("Exiting... 👋")
            break
        else:
            print("❌ Invalid option!")
if __name__ == "__main__":
    main()