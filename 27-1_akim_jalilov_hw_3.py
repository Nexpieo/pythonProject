class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__memory = value
    @property
    def memory(self):
        return  self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        print(self.__memory + self.__cpu)
    def __str__(self):
        return f'процессор:{self.cpu}, память:{self.memory}'
    def __eq__(self, other):
        return self.__memory == other.__memory
class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list
    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        print(f'Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number}')
    def __str__(self):
        return f'сим-карты:{self.sim_cards_list}'
class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)
    def use_gps(self, location):
        print(f'до локации {location} осталось 200 метров')
    def __str__(self):
        return f'процессор:{self.cpu}, память:{self.memory}, сим-карты:{self.sim_cards_list}'

computer1 = Computer(2.80, 8)
phone1 = Phone(['1-Beeline', '2-O!'])
smartphone1 = SmartPhone(3.20, 2, ['1-MegaCom'])
smartphone2 = SmartPhone(4.80, 4, ['1-O!','2-MegaCom'])
print(computer1)
print(phone1)
print(smartphone1)
print(smartphone2)

smartphone1.use_gps('Цум')
computer1.make_computations()
print(f"Is computer1's memory the same as smartphone1's:{computer1 == smartphone1}")
phone1.call(phone1.sim_cards_list[0], '0777006055')