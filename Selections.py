import pandas as pd
from math import isclose
from scipy.stats import shapiro


class Selectin:
    dictionary = None
    size = None
    Mx = None
    Mx2 = None
    Disp = None
    ASD = None
    corrected_D = None
    corrected_ASD = None
    asymmetry = None
    excess = None
    moda = None
    mediana = None

    def __init__(self, __data):
        sorted_tuple = sorted(__data.items(), key=lambda x: x[0])
        tmp_dict = dict(sorted_tuple)
        self.dictionary = tmp_dict
        self.size = self.get_count()

        self.Mx = self.get_Mx()
        self.Mx2 = self.get_Mx2()
        self.Disp = self.get_D()
        self.ASD = self.get_ASD()
        self.corrected_D = self.get_corrected_D()
        self.corrected_ASD = self.get_corrected_ASD()
        self.asymmetry = self.get_asymmetry()
        self.excess = self.get_excess()
        self.moda = self.get_Moda()
        self.mediana = self.get_Med()

    def get_count(self):
        count = 0
        for key in self.dictionary.keys():
            count += self.dictionary[key]
        return count

    def get_Mx(self):

        temp_Mx = 0
        for key in self.dictionary.keys():
            temp_Mx += int(key) * int(self.dictionary[key])

        return float(temp_Mx) / self.size

    def get_Mx2(self):
        temp_Mx = 0
        for key in self.dictionary.keys():
            temp_Mx += int(key) * int(key) * int(self.dictionary[key])

        return float(temp_Mx) / self.size

    def get_D(self):
        """
        находим дисперсию
        :param Mx:
        :param Mx2:
        :return:
        """
        return self.Mx2 - self.Mx ** 2

    def get_ASD(self):
        return self.Disp ** 0.5

    def get_corrected_D(self):
        return self.Disp * self.size / (self.size - 1)

    def get_corrected_ASD(self):
        return self.corrected_D ** 0.5

    def get_asymmetry(self):
        if self.Disp == 0:
            return 0
        asym_sum = 0
        for i in self.dictionary:
            asym_sum += (int(i) - self.Mx) ** 3

        res = (asym_sum / self.size) / (self.ASD ** 3)
        return res

    def get_excess(self):
        """
        эксцесс > 0 - островершие, <0 - плосковершие
        :param dictionary:
        :param _size:
        :param aver:
        :param asd:
        :return:
        """
        if self.Disp == 0:
            return 0
        asym_sum = 0
        for i in self.dictionary:
            asym_sum += (int(i) - self.Mx) ** 4

        res = (asym_sum / self.size) / (self.ASD ** 4) - 3
        return res

    def get_Moda(self):
        """
        находит моду
        :param dictionary: словарь: [элемент] = сколько раз встречается
        :return: ключ в словаре (Мода)
        """
        sorted_tuple = sorted(self.dictionary.items(), key=lambda x: -x[1])
        tmp_dict = dict(sorted_tuple)
        for i in tmp_dict:
            return i

    def get_Med(self):
        """
        находит медиану
        :param dictionary: словарь: [элемент] = сколько раз встречается
        :return: ключ в словаре (медиана)
        """
        half = self.size / 2
        half_counter = 0
        for i in self.dictionary.keys():
            half_counter += self.dictionary[i]
            if half_counter >= half:
                return i

    def output(self):
        return self.__dict__


def convert_from_disk_to_inter(__data, separator):
    if len(__data) < 2:
        raise ValueError('too little data')

    __data.sort()
    first = __data[0]
    last = __data[len(__data) - 1] + 1
    if first == last - 1:
        res = [{first: len(__data)}, first]
        return tuple(res)
    interval = (last - first) / separator
    step = first + interval

    inter_dict = {}
    interval_names = []
    inter_count = 0
    for i in __data:
        if i < step:
            inter_count += 1
        else:
            inter_dict[step - interval / 2] = inter_count
            interval_names.append("[" + str(step - interval) + "-" + str(step) + ")")
            inter_count = 0
            step += interval

    res = [inter_dict, interval_names]
    return tuple(res)


def Student(selection1, selection2, index):
    """
    t - критерий Cтьюдента
    :param selection1:
    :param selection2:
    :param index:
    :return:
    """
    if selection1.size != selection2.size:
        raise ValueError('different size')
    t_krit_empair = abs(selection1.Mx - selection2.Mx) / (
                selection1.Disp / selection1.size + selection2.Disp / selection2.size) ** 0.5

    studentData = pd.read_csv("Student.csv", delimiter=";")
    t_krit_table = studentData[index][selection1.size - 2]  # -1 на сдвиг с нуля и -1 на степень свободы
    res = [t_krit_empair, t_krit_table, isclose(t_krit_table - t_krit_empair, 0) or t_krit_table > t_krit_empair]
    return tuple(res)


def Fisher(selection1, selection2, index):
    """
    F - критерий фишера
    :param selection1:
    :param selection2:
    :param index:
    :return:
    """
    if selection1.size < 2 or selection2.size < 2:
        raise ValueError('too little data')

    disp1 = selection1.Disp
    disp2 = selection2.Disp
    f_empair = max(disp1, disp2) / min(disp1, disp2)
    fisherData = pd.read_csv("Fisher" + index + ".csv", delimiter=";")

    # большая столбец, меньшая по вертикали k = n-1
    if disp1 > disp2:
        k1 = selection1.size - 1
        k2 = selection2.size - 1
    else:
        k1 = selection2.size - 1
        k2 = selection1.size - 1

    f_table = fisherData[str(k1)][k2]
    res = [f_empair, f_table, isclose(f_table - f_empair, 0) or f_table > f_empair]
    return tuple(res)


def KS(selection1, selection2, index):
    """
    критерий Колмогорова-Смирнова
    :param selection1:
    :param selection2:
    :param index:
    :return:
    """
    if selection1.size != selection2.size:
        raise ValueError('different size')

    dmax = max(selection1.Mx - float(list(selection1.dictionary.keys())[0]), selection2.Mx - float(list(selection2.dictionary.keys())[0]))
    alfa_empair = dmax * (selection1.size**2/(2*selection1.size))**0.5

    KSData = pd.read_csv("KS2.csv", delimiter=";")
    if selection1.size < 36:
        alfa_krit = KSData[index][selection1.size - 1]
    else:
        if index == "0.01":
            alfa_krit = 1.63 * (2*selection1.size/selection1.size**2)**0.5
        else:
            alfa_krit = 1.36 * (2*selection1.size/selection1.size**2)**0.5

    res = [alfa_empair, alfa_krit, isclose(alfa_krit - alfa_empair, 0) or (alfa_krit > alfa_empair)]
    return tuple(res)


def Pirs(selection1, selection2):
    """
    Критерий Пирсона
    :param selection1:
    :param selection2:
    :return:
    """
    total_key_list = list(selection1.dictionary.keys()) + list(selection2.dictionary.keys())
    xi_empair = 0
    for key in total_key_list:
        if key not in selection1.dictionary.keys():
            tmp1 = 0
        else:
            tmp1 = selection1.dictionary[key]

        if key not in selection2.dictionary.keys():
            tmp2 = 0
        else:
            tmp2 = selection2.dictionary[key]

        xi_empair += ((selection1.size*tmp1 - selection2.size*tmp2)**2)/(tmp1 + tmp2)

    xi_empair = xi_empair/(selection1.size * selection2.size)

    XIData = pd.read_csv("XI2.csv", delimiter=";")
    breakin_free = (selection1.size - 1) * (selection2.size - 1)
    xi_krit_bigger = XIData["0.01"][breakin_free] / 10
    xi_krit_smaller = XIData["0.05"][breakin_free] / 10
    if xi_empair < xi_krit_smaller:
        confirmation = "True"
    elif xi_empair > xi_krit_bigger:
        confirmation = "False"
    else:
        confirmation = None

    res = [xi_empair, xi_krit_smaller, xi_krit_bigger, confirmation]
    return tuple(res)


def Shapiro_is_normal(selection):
    """
    тест Шапиро-Уилка на нормальность распределения
    :param selection:
    :return:
    """
    linear_data = []
    for i in selection.dictionary.keys():
        linear_data += [float(i)] * selection.dictionary[i]

    stat, p = shapiro(linear_data)

    res = ["Is normal: ", p < 0.05]
    return tuple(res)
