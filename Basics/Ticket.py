# Ticket Pricing & Access

print("-- WELCOME TO EVENT PORTAL --")

# Input section
try:
    age = int(input("Enter Your Age: "))
    is_student_input = input("Are you a Student? (yes/no): ").strip().lower()

    # Convert input into boolean (True / False)
    is_student = is_student_input == "yes"

    # Decision Logic (default values)
    discount = "No Discount"
    access = "General"
    message = ""

    if age < 0:
        message = "Invalid age entered."
        access = "None"

    elif age < 13:
        discount = "50% Child Discount"
        access = "Restricted (Guardian Required)"
        message = "Enjoy the kids zone!"

    elif age >= 65:
        discount = "30% Senior Discount"
        access = "Full Access"
        message = "Welcome! Priority seating is available."

    elif is_student:
        discount = "20% Student Discount"
        access = "Full Access"
        message = "Welcome! Please show your student ID."

    else:
        discount = "Standard Rate"
        access = "Full Access"
        message = "Welcome to the event."

    # Final Output
    print("\n--- Your Entry Details ---")
    print(f"Discount: {discount}")
    print(f"Access Level: {access}")
    print(f"Note: {message}")

except ValueError:
    print("Error: Please enter a valid number for age.")
