all_goods = []
goods_count = 0
name = input("введите название: ")

while name != "":
    price = int(input("price: "))
    count = int(input("count: "))
    unit = input("unit: ")
    goods_dictionary = {
        "название": name,
        "цена": price,
        "количество": count,
        "ед": unit,
    }
    goods_count += 1
    all_goods.append((goods_count, goods_dictionary))
    name = input("name: ")

print(all_goods)

goods_dict = {"название": [], "цена": [], "количество": [], "ед": set()}
for i in all_goods:
    n = i[1]
    goods_dict["название"].append(n["название"])
    goods_dict["цена"].append(n["цена"])
    goods_dict["количество"].append(n["количество"])
    goods_dict["ед"].add(n["ед"])
    # for key in n:
    # goods_dict[key].append(n[key])
print(goods_dict)
