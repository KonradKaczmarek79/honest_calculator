class Calculator:
    messages = {
        "msg_0": "Enter an equation\n",
        "msg_1": "Do you even know what numbers are? Stay focused!",
        "msg_2": "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        "msg_3": "Yeah... division by zero. Smart move...",
        "msg_4": "Do you want to store the result? (y / n):\n",
        "msg_5": "Do you want to continue calculations? (y / n):\n",
    }
    operators = {"+", "-", "*", "/", "//", "%", }

    def __init__(self, memory=0):
        self.memory = memory
        self.number_one = None
        self.number_two = None
        self.operator = None
        self.data_correct = False
        self.result = None

    def __repr__(self):
        return str(self.__dict__)

    def check_operator(self, operator):
        if operator not in self.operators:
            raise ValueError
        return operator

    @staticmethod
    def add_numbers(a: int | float, b: int | float) -> int | float:
        return a + b

    @staticmethod
    def substract_numbers(a: int | float, b: int | float) -> int | float:
        return a - b

    @staticmethod
    def multiply_numbers(a: int | float, b: int | float) -> int | float:
        return a * b

    @staticmethod
    def divide_numbers(a: int | float, b: int | float) -> int | float:
        return a / b

    def should_result_be_stored(self, result):
        self.memory = result if input(self.messages["msg_4"]) == "y" else self.memory
        self.result = None
        self.number_one = None
        self.number_two = None
        self.operator = None


    def calculation(self):
        if self.operator == "+":
            self.result = self.add_numbers(self.number_one, self.number_two)
        elif self.operator == "-":
            self.result = self.substract_numbers(self.number_one, self.number_two)
        elif self.operator == "*":
            self.result = self.multiply_numbers(self.number_one, self.number_two)
        elif self.operator == "/":
            try:
                self.result = self.divide_numbers(self.number_one, self.number_two)
            except ZeroDivisionError:
                print(self.messages["msg_3"])
                self.data_correct = False
                return
        print(self.result)

        self.should_result_be_stored(self.result)


    def check_num_value(self, val):
        if val == "M":
            val = self.memory
        else:
            val = float(val)
        return val


    def insert_data(self):
        temp_data = input(self.messages["msg_0"])
        temp_data = temp_data.split(" ")
        try:
            temp_data[0] = self.check_num_value(temp_data[0])
            temp_data[2] = self.check_num_value(temp_data[2])
        except ValueError:
            print(self.messages["msg_1"])
            return

        try:
            self.operator = self.check_operator(temp_data[1])
        except ValueError:
            print(self.messages["msg_2"])
            return
        else:
            self.number_one = float(temp_data[0])
            self.number_two = float(temp_data[2])
            self.data_correct = True


def main():
    repeat = True
    calc = Calculator()

    while repeat:
        calc.insert_data()
        if calc.data_correct:
            calc.calculation()
        if calc.data_correct:
            repeat = True if input("Do you want to continue calculations? (y / n):\n") == "y" else False


if __name__ == "__main__":
    main()
