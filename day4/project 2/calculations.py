def Calculations():
    try:
        subject1 = float(input("Enter the marks for C: "))
        if subject1 < 0 or subject1 > 100:
            raise ValueError("Marks should be between 0 and 100.")
        
        subject2 = float(input("Enter the marks for C++: "))
        if subject2 < 0 or subject2 > 100:
            raise ValueError("Marks should be between 0 and 100.")
        
        subject3 = float(input("Enter the marks for Java: "))
        if subject3 < 0 or subject3 > 100:
            raise ValueError("Marks should be between 0 and 100.")
        
        subject4 = float(input("Enter the marks for Python: "))
        if subject4 < 0 or subject4 > 100:
            raise ValueError("Marks should be between 0 and 100.")

        print("Marks added")
        print("Now you can Check the CSV file")
        print("-----Thanks for using-----")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return Calculations()

    average_marks_obtained = (subject1 + subject2 + subject3 + subject4) / 4
    #rounded_average_marks_obtained=round({average_marks_obtained},2)
    rounded_average_marks_obtained="{:.2f}".format(average_marks_obtained)


    if average_marks_obtained < 50:
        Grade = "Fail"
    elif 50 <= average_marks_obtained < 60:
        Grade = "C+"
    elif 60 <= average_marks_obtained < 70:
        Grade = "B"
    elif 70 <= average_marks_obtained < 80:
        Grade = "B+"
    elif 80 <= average_marks_obtained < 90:
        Grade = "A"
    elif 90 <= average_marks_obtained <= 100:
        Grade = "A+"

    return subject1, subject2, subject3, subject4, rounded_average_marks_obtained, Grade

