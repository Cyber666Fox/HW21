from classes import Request, storage_1, storage_2, shop_1

print("Привет!")

while True:
    print ("На склад(е/ах) хранится:")
    print(f"storage_1: {storage_1}")
    print(f"storage_2: {storage_2}")

    print ("В магазине хранится:")
    print(f"shop_1: {shop_1}")

    user_text = input("Введите команду:\n")
    

    if user_text == "стоп":
        break
    else:
        try:
            req = Request(user_text)
            req.move()
        except Exception as e:
            print(f"Произошла ошибка {e}, ни чего страшного, продолжайте")