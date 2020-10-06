weight = float(input("ENTER WEIGHT(in kgs):"))
height = float(input("ENTER HEIGHT(in metres):"))
BMI = (weight)/(height*height) 
if(BMI<18.5):
   print("Underweight, BMI =",BMI)
elif(BMI>=18.5 and BMI<25):
   print("Normal, BMI =",BMI)
elif(BMI>=25 and BMI<30):
   print("Overweight, BMI =",BMI)
elif (BMI>=30):
   print("Obese, BMI =",BMI)
