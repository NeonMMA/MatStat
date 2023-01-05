import Selections as sel
from collections import Counter
from prettytable import PrettyTable
x = PrettyTable()

data = [0, 3, 5, 4, 3, 0, 5, 3, 3, 7, 4, 4, 4, 8, 3]
data2 = [0, 3, 5, 4, 3, 0, 5, 0, 3, 7, 4, 4, 4, 8, 3]

# first_class = Selectin(data, 1)
# second_class = Selectin(data2, 1)

interval_dict1, interval_dict_names = sel.convert_from_disk_to_inter(data, 4)
interval_dict2, interval_dict_names2 = sel.convert_from_disk_to_inter(data2, 4)

data_dict1 = dict(Counter(data))
data_dict2 = dict(Counter(data2))

x = PrettyTable()
x.field_names = interval_dict_names
x.add_row(interval_dict1.values())

# fig, (ax1, ax2) = plt.subplots(1, 2)
# fig.suptitle('Horizontally stacked subplots')
# ax1.plot(data_dict1.keys(), data_dict1.values())
# ax2.plot(data_dict2.keys(), data_dict2.values())
# plt.show()
# fig, (ax1, ax2) = plt.subplots(1, 2)
# fig.suptitle('Horizontally stacked subplots')
# ax1.bar(interval_dict_names, interval_dict1.values())
# ax2.bar(interval_dict_names2, interval_dict2.values())
# plt.show()

first_class = sel.Selectin(interval_dict1)
second_class = sel.Selectin(interval_dict2)
print(first_class.output())

print(sel.Student(first_class, second_class, "0.05"))
print(sel.Fisher(first_class, second_class, "0.05"))
print(sel.KS(first_class, second_class, "0.05"))
print(sel.Pirs(first_class, second_class))

# print(sel.Shapiro_is_normal(first_class))

# print(x)