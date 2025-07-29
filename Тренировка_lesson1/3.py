from user import User
from card import Card

alex = User("Alex")

alex.sayName()
alex.setAge(33)
alex.sayAge()

card = Card("1234 3223 3443 4554", "11/28", "Alex F")

alex.addCard(card)
alex.getCard().pay(1000)
