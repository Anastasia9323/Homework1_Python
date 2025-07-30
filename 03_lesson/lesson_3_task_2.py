from smartphone import Smartphone


catalog = [
        Smartphone(brand="Samsung", model="A5", number="+79876545676"),
        Smartphone(brand="Apple", model="13", number="+79876545676"),
        Smartphone(brand="Xiaomi", model="S2", number="+79875674554"),
        Smartphone(brand="Honor", model="B5", number="+76787654567"),
        Smartphone(brand="Poco", model="Q1", number="+78766789098")
        ]

for Smartphone in catalog:
    print(f"{Smartphone.brand} - {Smartphone.model}. {Smartphone.number} ")

