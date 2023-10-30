def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height*height)

    print("Bmi = " + str(bmi))

    if(bmi<18.5):
        print("You are Under Weight")
        w = -1

    elif(18.5<bmi<=25.0):
        print("You are Normal Weight")
        w = 0

    elif(25.0<bmi):
        print("You are Over Weight")
        w = 1


calculate_bmi(height=1.73, weight=57)
