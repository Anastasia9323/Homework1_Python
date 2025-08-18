from Address import Address
from Mailing import Mailing

to_address = Address("646503", "Омск", "ул. Пушкина", "10", "кв. 1")

from_address = Address("657654", "Москва", "ул. Лермонтова", "34", "кв. 24")

mailing = Mailing("12345", from_address, to_address, 500)

print(mailing)
