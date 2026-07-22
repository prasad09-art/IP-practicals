age = int(input("enter your age:"))
nationality = input(" Enter your nationality:")

if age >= 18:
    if nationality.lower() == "indian":
        print("Eligibel to vote")
    else:
        print("Not Eligible to vote(Only Indian citizens can vote)")


else:
     print("Not eligible to vote(age must be 18 or above)")
