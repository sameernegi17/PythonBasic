number_1 = int(input("Enter the number 1"))
number_2 = int(input("Enter the number 1"))
number_3 = int(input("Enter the number 3"))


if(number_1 >= number_2 and number_1 >= number_3):
    print("Greatest Number {}".format(number_1))
elif(number_2 >= number_1 and number_2 >= number_3):
    print("Greatest Number {}".format(number_2))
else:
    print("Greatest Number {}".format(number_3))