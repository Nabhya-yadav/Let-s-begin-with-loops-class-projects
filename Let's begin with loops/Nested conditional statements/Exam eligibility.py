medicalcert=(input("Do u have a medical certifacte(y or n)"))

if medicalcert=="n":
    print("Not eligible for exam")

else:
    print("Eligible for exam")

    att=int(input("Enter the percent of attendence"))
    if att>=75:
        print("allowed for exam")

    else:
        print("Not allowed for exam")

    

