from smartphone import Smartphone

# Создаем список для каталога
catalog = []

# Наполняем список пятью разными экземплярами
catalog.append(Smartphone("Apple", "iPhone 15 Pro", "+7-953-595-12-72"))
catalog.append(Smartphone("Samsung", "Galaxy S24 Ultra", "+7-911-234-56-78"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 13", "+7-999-345-67-89"))
catalog.append(Smartphone("Google", "Pixel 8", "+7-981-456-78-90"))
catalog.append(Smartphone("OnePlus", "12", "+7-495-567-89-01"))

# Печатаем каталог в нужном формате
print("Каталог смартфонов:")
print("-" * 40)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")