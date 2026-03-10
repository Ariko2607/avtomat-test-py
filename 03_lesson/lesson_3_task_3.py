from address import Address
from mailing import Mailing

# Создаем адрес отправителя
from_address = Address(
    index="123456",
    city="Москва",
    street="Тверская",
    house="15",
    apartment="42"
)

# Создаем адрес получателя
to_address = Address(
    index="654321",
    city="Санкт-Петербург",
    street="Невский проспект",
    house="28",
    apartment="15"
)

# Создаем почтовое отправление
mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=350.50,
    track="RU123456789CN"
)

# Выводим информацию об отправлении в требуемом формате
print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")