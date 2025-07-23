rate_as_str = input("Оцените работу оператора от 1 до 5:")
rate = int(rate_as_str)

if(rate < 1):
    rate = 1

if(rate > 5):
    rate = 5

feedback = ''

if rate == 1:
    feedback = input("расскажите что улучшить")
elif rate == 2:
    feedback = input("расскажите что смиутило")
elif rate == 3:
    feedback = input("расскажите как лучше")
elif rate == 4:
    feedback = input("расскажите почему не 5")
else:
    feedback = input("расскажите за что похвалить")

print(feedback)