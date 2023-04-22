class computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('Device', self.cpu, self.ram)

com1 = computer('i5', 500)
com2 = computer('i9','64gb')

com1.config()
com2.config()










