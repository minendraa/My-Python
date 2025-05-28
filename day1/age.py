"""Create a program that asks the user for their age and prints whether they are a minor (under 18), an adult (18 to 60), or a senior (above 60)."""
age = int(input("Enter your age: "))

if age < 18:
    print("minor")
elif 18 <= age <= 60:
    print("adult")
else:
    print("senior")
