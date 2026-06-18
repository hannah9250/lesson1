def shutdown(choice):
    if choice == "yes":
        return "Shutting down"
    elif choice == "no":
        return "Abort shutdown"
    else:
        return "Sorry"

choice = input("Enter Yes or No: ")
print(shutdown(choice))