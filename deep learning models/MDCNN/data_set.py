# -*- coding: utf-8 -*-

from collections import namedtuple

Data_set = namedtuple('Data_set',['name','classes_num','train_size','test_size','length'])


AppliancesEnergy = Data_set(name='AppliancesEnergy', classes_num=1, train_size=96, test_size=42, length=144)

data_set_dict = {'AppliancesEnergy':AppliancesEnergy}
