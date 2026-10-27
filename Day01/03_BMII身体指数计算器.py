h=float((input("请输入身高(m)：")))
w=float((input("请输入体重(kg)：")))
BMI=w/(h*h)
if(BMI<19.5):
    print("偏瘦")
if(BMI>=18.5 and BMI<24):
    print("正常")
if(BMI>=24):
    print("偏胖")