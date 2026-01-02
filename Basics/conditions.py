#small decision program for conditions practice
age = int(input("Please enter your age: "))
student = input("Are you student (Yes/No): ").lower()

if age > 60:
    print("Senior citizen discount 60%.")

elif age < 18 or student == "Yes":
    print("Free Entry.")

elif age > 18 or student == "Yes":
    print("YOu get 50% discount.")

elif student != "Yes" and student != "No":
    print("Invalid input!!")    

else:
    print("You pay full price.")


