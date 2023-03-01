'''能耗换算'''


class UnitConvert:
    def convert_ES(self, n, unit1, unit2):
        c = [1000, 700]
        l = ['千克标油', '千克标煤']
        if unit1 not in l or unit2 not in l:
            result = 0
        else:
            unit1_index = l.index(unit1)
            unit2_index = l.index(unit2)
            print(type(n))
            print(n.get())
            num=int(n.get())
            result = num/c[unit1_index]*c[unit2_index]
        return result

    '''热量单位换算'''
    def convert_E(self, n,unit1,unit2):
        c = [0.2389, 1, 1000, 1000000, 1000000000, 1000000000000]
        l = ['kcal', 'KJ', 'MJ', 'GJ', 'TJ']
        if unit1 not in l or unit2 not in l:
            result = 0
        else:
            unit1_index = l.index(unit1)
            unit2_index = l.index(unit2)
            print(type(n))
            print(n.get())
            num = int(n.get())
            result = num / c[unit1_index] * c[unit2_index]
        return result

    '''长度单位换算'''
    def convert_L(self, n,unit1,unit2):
        c = [1000, 100, 10, 1, 0.001]
        l = ['毫米', '厘米', '分米', '米', '千米' ]
        if unit1 not in l or unit2 not in l:
            result = 0
        else:
            unit1_index = l.index(unit1)
            unit2_index = l.index(unit2)
            print(type(n))
            print(n.get())
            num = int(n.get())
            result = num / c[unit1_index] * c[unit2_index]
        return result

    def choose_unit(self, envet):
        choose = box1.get()
        list=[]
        print(choose)
        if choose == '能耗':
            list = ['千克标油', '千克标煤']
        elif choose == '长度':
            list = ['厘米', '分米', '米', '千米', '毫米']
        elif choose == '热量':
            list = ['kcal', 'KJ','MJ','GJ','TJ']
        box2['value'] = list
        box3['value'] = list

    '''选择单位后的触发事件，计算的结果出现在如下情况：选择了正确的单位，或者输入数字后回车'''
    def convert(self, envet):
        global data
        global data_out
        unit_class = box1.get()
        if unit_class == '能耗':
            data_out.set(self.convert_ES(data, box2.get(),box3.get()))
        elif unit_class =='长度':
            data_out.set(self.convert_L(data, box2.get(), box3.get()))
        elif unit_class =='热量':
            data_out.set(self.convert_E(data, box2.get(), box3.get()))
        label4.update()

    def result(self):
        try:
            if inp.get() == "":
                inp.insert("end", "error")
            elif inp.get()[0] == "0":
                inp.delete(0, "end")
                inp.insert("end", "error")
            else:
                res = inp.get()
                res = eval(res)
                inp.insert("end", " = ")
                inp.insert("end", res)
        except SyntaxError:
            inp.insert("end", "invalid input")