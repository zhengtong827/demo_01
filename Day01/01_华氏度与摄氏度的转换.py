# 华氏度和摄氏度的转换
# 1.华氏度转为摄氏度
fahrenheit = float(input("请输入华氏度："))
celsius = (fahrenheit - 32) * 5 / 9
print("摄氏度为：", celsius)
# 2.摄氏度转为华氏度
celsius = float(input("请输入摄氏度："))
fahrenheit = (celsius * 9 / 5) + 32
print("华氏度为：", fahrenheit)
