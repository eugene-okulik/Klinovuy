PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_dict = {name: int(price[:-1]) for name, price in (element.split(' ', 1)
            for element in PRICE_LIST.splitlines())}

print(new_dict)
