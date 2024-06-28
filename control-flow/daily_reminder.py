def main():
    # Prompting user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Match Case for priority
    match priority:
        case 'high':
            priority_message = "is a high priority task"
        case 'medium':
            priority_message = "is a medium priority task"
        case 'low':
            priority_message = "is a low priority task"
        case _:
            print("Invalid priority entered. Please choose high, medium, or low.")
            return

    # Handling time-bound condition
    if time_bound == 'yes':
        time_bound_message = "that requires immediate attention today!"
    elif time_bound == 'no':
        time_bound_message = "Consider completing it when you have free time."
    else:
        print("Invalid input for time-bound. Please enter yes or no.")
        return

    # Printing the reminder message
    print(f"\nReminder: '{task}' {priority_message} {time_bound_message}")

if __name__ == "__main__":
    main()

