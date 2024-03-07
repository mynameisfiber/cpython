items_list = []
items_dict = dict()
items_set = set()
for i in range(1 << 8):
    items_list.append(i)
    items_dict[i] = True
    items_set.add(i)
    print(
        f"{i=}\t{items_list.allocated()=}\t{items_dict.allocated()=}\t{items_set.allocated()=}"
    )
