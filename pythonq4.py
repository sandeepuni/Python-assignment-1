
speed = []
print("Please enter the 12 speeds")
for i in range(12):
    speed.append(float(input(f"Enter speed for hour {i+1}: ")))

Average = sum(speed)/12
if Average < 40 :
   print("Slow")
elif 40 <= Average <=80 :
    print("Normal")
else :
    print("Fast")
44
