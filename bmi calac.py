import colorama
from colorama import Fore


height=input("Enter your height in m:")
weight=input("Enter your weight in kgs:")

bmi= int(weight)/float(height)**2

print("Your BMI is : "+str(round(bmi,2)))

if bmi<18.5:
    print(Fore.WHITE+"You are under weight")
elif 18.5<=bmi<25:
    print(Fore.GREEN+"You have a normal weight")
elif 25<=bmi<30:
    print(Fore.YELLOW+"You are over weight")
elif 30<=bmi<35:
    print(Fore.LIGHTRED_EX+"You are obese")
else:
    print(Fore.RED+"You are clinically obese")


