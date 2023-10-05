"""
請輸入身高:1.7
請輸入體重:50
你的BMI為17.301038062283737
"""
h = float(input("身高="))
w = float(input("體重="))
bmi = w / h**2
print("你的BMI為" + str(bmi))

if 16.4 <= bmi <= 21.5:
    print("normal")
elif bmi > 21.5:
    print("u are so fat")
elif bmi < 16.4:
    print(" u eat dirt")