medical_cause=input("Did you have a medical cause? Y or N")
atten=int(input("Enter the attendance of the student: "))
if medical_cause=="Y":
    print("You're allowewd")
else:
    if atten>=75:
        print("Allowed")
    else:
        print("Not allowed")
