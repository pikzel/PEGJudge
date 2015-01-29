m = float(input())
h = float(input())
bmi = m/(h*h)
if bmi < 18.5:
	print('Underweight')
elif bmi > 25:
	print('Overweight')
else:
	print('Normal weight')
