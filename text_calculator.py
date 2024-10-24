import math


def text_calculator(s):
    s = s.replace("одна", "один").replace("одной","одного").replace("десятую", "десятых").replace("сотую", "сотых").replace("тысячную",
                                                                                                  "тысячных").replace(
        "одну", "один").replace("сотая", "сотых").replace("две ", "два ").replace("десятая",
                                                                                  "десятых").replace(
        "тысячная", "тысячных").split()

    # print(s)

    def converting_str_to_int(s, k):
        hundreds = 0
        if s[k] in unit1:
            unit = unit1[s[k]]
            tens = 0
            k += 1
        elif s[k] in hundreds1:
            hundreds = hundreds1[s[k]]
            if (k + 1) >= len(s) or s[k + 1] not in tens1:
                if (k + 1) >= len(s) or s[k + 1] not in unit1:
                    unit = 0
                    tens = 0
                    k += 1
                else:
                    tens = 0
                    unit = unit1[s[k + 1]]
                    k += 2
            else:
                tens = tens1[s[k + 1]]
                k += 1
                if (k + 1) >= len(s) or s[k + 1] not in unit1:
                    unit = 0
                else:
                    unit = unit1[s[k + 1]]
                k += 2

        else:
            if (k + 1) >= len(s) or s[k + 1] not in unit1:
                unit = 0
                tens = tens1[s[k]]
                k += 1
            else:
                unit = unit1[s[k + 1]]
                tens = tens1[s[k]]
                k += 2
        if unit > 9:
            tens += 1
            unit = unit % 10
        a = hundreds * 100 + tens * 10 + unit
        return a, k

    def converting_str_to_int3(s, k):
        hundreds = 0
        if s[k] in unit3:
            unit = unit3[s[k]]
            tens = 0
            k += 1
        elif s[k] in hundreds3:
            hundreds = hundreds3[s[k]]
            if (k + 1) >= len(s) or s[k + 1] not in tens3:
                if (k + 1) >= len(s) or s[k + 1] not in unit3:
                    unit = 0
                    tens = 0
                    k += 1
                else:
                    tens = 0
                    unit = unit3[s[k + 1]]
                    k += 2
            else:
                tens = tens3[s[k + 1]]
                k += 1
                if (k + 1) >= len(s) or s[k + 1] not in unit3:
                    unit = 0
                else:
                    unit = unit3[s[k + 1]]
                k += 2

        else:
            if (k + 1) >= len(s) or s[k + 1] not in unit3:
                unit = 0
                tens = tens3[s[k]]
                k += 1
            else:
                unit = unit3[s[k + 1]]
                tens = tens3[s[k]]
                k += 2
        if unit > 9:
            tens += 1
            unit = unit % 10
        a = hundreds * 100 + tens * 10 + unit
        return a, k

    def converting_int_to_str(result):
        result_arr = []
        if result < 0:
            result_arr.append("минус")
        if abs(result) < 20:
            result_arr.append(unit2[abs(result)])
        if abs(result) >= 20 and abs(result) < 100:
            result_arr.append(tens2[abs(result) // 10])
            if unit2[abs(result) % 10] != "ноль":
                result_arr.append(unit2[abs(result) % 10])
        if abs(result) >= 100:
            result_arr.append(hundreds2[abs(result) // 100])
            if abs(result) % 100 // 10 in tens2.keys():
                result_arr.append(tens2[abs(result) % 100 // 10])
            if abs(result) % 100 in (10, 11, 12, 13, 14, 15, 16, 17, 18, 19):
                result_arr.append(unit2[abs(result) % 100])
            if abs(result) % 10 > 0 and abs(result) % 100 not in (10, 11, 12, 13, 14, 15, 16, 17, 18, 19):
                result_arr.append(unit2[abs(result) % 10])

        return (" ".join(result_arr))

    unit1 = {i: j for j, i in enumerate(
        "ноль один два три четыре пять шесть семь восемь девять десять одиннадцать двенадцать тринадцать четырнадцать пятнадцать шестнадцать семнадцать восемнадцать девятнадцать".split(),
        0)}
    tens1 = {i: j for j, i in
             enumerate("двадцать тридцать сорок пятьдесят шестьдесят семьдесят восемьдесят девяносто".split(), 2)}
    hundreds1 = {i: j for j, i in
                 enumerate("сто двести триста четыреста пятьсот шестьсот семьсот восемьсот девятьсот".split(), 1)}
    unit2 = {j: i for j, i in enumerate(
        "ноль один два три четыре пять шесть семь восемь девять десять одиннадцать двенадцать тринадцать четырнадцать пятнадцать шестнадцать семнадцать восемнадцать девятнадцать".split(),
        0)}
    tens2 = {j: i for j, i in
             enumerate("двадцать тридцать сорок пятьдесят шестьдесят семьдесят восемьдесят девяносто".split(), 2)}
    hundreds2 = {j: i for j, i in
                 enumerate("сто двести триста четыреста пятьсот шестьсот семьсот восемьсот девятьсот".split(), 1)}

    unit3 = {i: j for j, i in enumerate(
        "ноля одного двух трех четырех пяти шести семи восьми девяти десяти одиннадцати двенадцати тринадцати четырнадцати пятнадцати шестнадцати семнадцати восемнадцати девятнадцати".split(),
        0)}
    tens3 = {i: j for j, i in
             enumerate("двадцати тридцати сорока пятьдесяти шестьдесяти семьдесяти восемьдесяти девяноста".split(), 2)}
    hundreds3 = {j: i for j, i in
                 enumerate("ста двухсот трехсот четырехсот пятисот шестисот семисот восьмисот девятисот".split(), 1)}
    k = 0
    result = 0
    if s[k] not in ("синус", "косинус", "тангенс"):
        a, k = converting_str_to_int(s, k)
        oper = s[k]
        if oper == "умножить" or oper == "разделить" or oper == "и" or oper == "в":
            k += 1
        if oper == "и":
            dr_ch1, k = converting_str_to_int(s, k)
            k += 1
            if s[k - 1] == "десятых":
                a += dr_ch1 / 10
            elif s[k - 1] == "сотых":
                a += dr_ch1 / 100
            elif s[k - 1] == "тысячных":
                a += dr_ch1 / 1000
            oper = s[k]
            if oper == "умножить" or oper == "разделить":
                k += 1

        k += 1
        b, k = converting_str_to_int(s, k)
        if k < len(s) and s[k] == "и":
            k += 1
            dr_ch1, k = converting_str_to_int(s, k)
            if s[k] == "десятых":
                b += dr_ch1 / 10
            elif s[k] == "сотых":
                b += dr_ch1 / 100
            elif s[k] == "тысячных":
                b += dr_ch1 / 1000

        result = 0
        if oper == "плюс":
            result = a + b
        elif oper == "минус":
            result = a - b
        elif oper == "умножить":
            result = a * b
        elif oper == "разделить":
            result = a / b
        elif oper == "в":
            result = a ** b


    else:
        oper = s[k]
        k += 2
        if s[k] != "пи":
            if s[k] in unit1 or s[k] in tens1 or s[k] in hundreds1:
                a, k = converting_str_to_int(s, k)
                if k < len(s) and s[k] == "и":
                    k += 1
                    dr_ch1, k = converting_str_to_int(s, k)
                    if s[k] == "десятых" or s[k] == "десятой":
                        a += dr_ch1 / 10
                    elif s[k] == "сотых" or s[k] == "сотой":
                        a += dr_ch1 / 100
                    elif s[k] == "тысячных" or s[k] == "тысячной":
                        a += dr_ch1 / 1000
                    k += 1
                if k < len(s):
                    oper2 = s[k]
                    k += 1
                    if oper2 == "умножить" or oper2 == "разделить" or oper2 == "в":
                        k += 1
                    b, k = converting_str_to_int(s, k)
                    if k < len(s) and s[k] == "и":
                        k += 1
                        dr_ch1, k = converting_str_to_int(s, k)
                        if s[k] == "десятых":
                            b += dr_ch1 / 10
                        elif s[k] == "сотых":
                            b += dr_ch1 / 100
                        elif s[k] == "тысячных":
                            b += dr_ch1 / 1000
                        k += 1

                    result = 0

                    if oper2 == "плюс":
                        result = a + b
                    elif oper2 == "минус":
                        result = a - b
                    elif oper2 == "умножить":
                        result = a * b
                    elif oper2 == "разделить":
                        result = a / b
                    elif oper2 == "в":
                        result = a ** b

                if oper == "синус":
                    result = round(math.sin(result), 3)
                elif oper == "косинус":
                    result = round(math.cos(result), 3)
                elif oper == "тангенс":
                    result = round(math.tan(result), 3)

            else:
                a, k = converting_str_to_int3(s, k)
                if k < len(s) and s[k] == "и":
                    k += 1
                    dr_ch1, k = converting_str_to_int3(s, k)
                    if s[k] == "десятых" or s[k] == "десятой":
                        a += dr_ch1 / 10
                    elif s[k] == "сотых" or s[k] == "сотой":
                        a += dr_ch1 / 100
                    elif s[k] == "тысячных" or s[k] == "тысячной":
                        a += dr_ch1 / 1000
                    k += 1
                if k < len(s):
                    oper2 = s[k]
                    k += 1
                    if oper2 == "умножить" or oper2 == "разделить" or oper2 == "в":
                        k += 1
                    b, k = converting_str_to_int(s, k)
                    if k < len(s) and s[k] == "и":
                        k += 1
                        dr_ch1, k = converting_str_to_int(s, k)
                        if s[k] == "десятых":
                            b += dr_ch1 / 10
                        elif s[k] == "сотых":
                            b += dr_ch1 / 100
                        elif s[k] == "тысячных":
                            b += dr_ch1 / 1000
                        k += 1

                    result = 0
                    if oper == "синус":
                        result = round(math.sin(a), 3)
                    elif oper == "косинус":
                        result = round(math.cos(a), 3)
                    elif oper == "тангенс":
                        result = round(math.tan(a), 3)

                    if oper2 == "плюс":
                        result = result + b
                    elif oper2 == "минус":
                        result = result - b
                    elif oper2 == "умножить":
                        result = result * b
                    elif oper2 == "разделить":
                        result = result / b
                    elif oper2 == "в":
                        result = result ** b
                else:
                    if oper == "синус":
                        result = round(math.sin(a), 3)
                    elif oper == "косинус":
                        result = round(math.cos(a), 3)
                    elif oper == "тангенс":
                        result = round(math.tan(a), 3)


        else:
            a = math.pi
            k += 1
            if k < len(s):
                oper2 = s[k]
                k += 1
                if oper2 == "умножить" or oper2 == "разделить" or oper2 == "в":
                    k += 1
                b, k = converting_str_to_int(s, k)
                if k < len(s) and s[k] == "и":
                    k += 1
                    dr_ch1, k = converting_str_to_int(s, k)
                    if s[k] == "десятых":
                        b += dr_ch1 / 10
                    elif s[k] == "сотых":
                        b += dr_ch1 / 100
                    elif s[k] == "тысячных":
                        b += dr_ch1 / 1000

                result = 0
                if oper2 == "плюс":
                    result = a + b
                elif oper2 == "минус":
                    result = a - b
                elif oper2 == "умножить":
                    result = a * b
                elif oper2 == "разделить":
                    result = a / b
                elif oper2 == "в":
                    result = a ** b
                if oper == "синус":
                    result = round(math.sin(result), 3)
                elif oper == "косинус":
                    result = round(math.cos(result), 3)
                elif oper == "тангенс":
                    result = round(math.tan(result), 3)
            else:
                if oper == "синус":
                    result = round(math.sin(a), 3)
                elif oper == "косинус":
                    result = round(math.cos(a), 3)
                elif oper == "тангенс":
                    result = round(math.tan(a), 3)


    if isinstance(result, int) or result.is_integer():
        result_str = converting_int_to_str(result)
    else:
        result_str1 = str(result)
        int_p, fl_p = result_str1.split(".")
        int_p = int(int_p)
        fl_p = str(fl_p)[:4]
        # print(fl_p)
        if len(fl_p) == 1:
            if int(fl_p) % 10 == 1:
                t = " десятая"
            else:
                t = " десятых"

        elif len(fl_p) == 2:
            if int(fl_p) % 10 == 1 and int(fl_p) != 11:
                t = " сотая"
            else:
                t = " сотых"

        else:
            if len(fl_p) > 3:
                fl_p = round(int(fl_p) / 10)
            if int(fl_p) % 10 == 1 and int(fl_p) != 11:
                t = " тысячная"
            else:
                t = " тысячных"
        flg = False
        if int(fl_p) % 10 == 2 and int(fl_p) != 12:
            flg = True

        fl_p = int(fl_p)
        result_str = converting_int_to_str(int_p)
        result_str += " и "
        fl_p_str = converting_int_to_str(fl_p)
        if t == " десятая" or t == " сотая" or t == " тысячная":
            fl_p_str = fl_p_str.replace("один", "одна")
        fl_p_str += t
        if flg:
            fl_p_str = fl_p_str.replace("два ", "две ")

        result_str += fl_p_str
        if result < 0:
            result_str = "минус " + result_str

    return result_str


s = input()
print(text_calculator(s))
