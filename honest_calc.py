class Calculator:
    """Create the Calculator instance to perform the calculations, and it will respond with 'honest' replies."""

    # class field messages contains all possible messages you may get during calculations
    messages = {
        "msg_0": "Enter an equation\n",
        "msg_1": "Do you even know what numbers are? Stay focused!",
        "msg_2": "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        "msg_3": "Yeah... division by zero. Smart move...",
        "msg_4": "Do you want to store the result? (y / n):\n",
        "msg_5": "Do you want to continue calculations? (y / n):\n",
        "msg_6": " ... lazy",
        "msg_7": " ... very lazy",
        "msg_8": " ... very, very lazy",
        "msg_9": "You are",
        "msg_10": "Are you sure? It is only one digit! (y / n)\n",
        "msg_11": "Don't be silly! It's just one number! Add to the memory? (y / n)\n",
        "msg_12": "Last chance! Do you really want to embarrass yourself? (y / n)\n",
    }

    # possible operators
    operators = {"+", "-", "*", "/", "//", "%", }

    def __init__(self, memory=0):
        """The initializer for the class.

        :param memory: initial state of calculator memory
        """
        self.memory = memory
        self.number_one = None
        self.number_two = None
        self.operator = None
        self.data_correct = False
        self.result = None

    def __repr__(self):
        """Calculator instance representation

        :return: dict with class fields
        """
        return str(self.__dict__)

    def check_operator(self, operator):
        """
        Check if the operator is a valid value according to the definition in self.operators ones.
        :param operator: string value to check
        :return: operator if it is valid, raise ValueError otherwise
        """
        if operator not in self.operators:
            raise ValueError
        return operator

    @staticmethod
    def add_numbers(a: int | float, b: int | float) -> int | float:
        """simple addition operation

        :param a: first number
        :param b: second number
        :return: a + b result
        """
        return a + b

    @staticmethod
    def substract_numbers(a: int | float, b: int | float) -> int | float:
        """simple subtraction operation

        :param a: first number
        :param b: second number
        :return: a - b result
        """
        return a - b

    @staticmethod
    def multiply_numbers(a: int | float, b: int | float) -> int | float:
        """Simple multiplication operation

        :param a: first number
        :param b: second number
        :return: a * b result
        """
        return a * b

    @staticmethod
    def divide_numbers(a: int | float, b: int | float) -> int | float:
        """Simple division operation

        :param a: first number
        :param b: second number
        :return: a / b result"""
        return a / b

    def storage_confirmation(self, result, msg_index=10):
        """Ask the user whether he/she would like to continue. If the answer is 'y' ask again (no more than 3 times).
        A user can change their mind or confirm his/her choice three times before the result is saved in memory.

        :param result: numeric value to check
        :param msg_index: index used to select the appropriate message for the user
        :return: value to set in memory if it's valid current memory state otherwise
        """
        answer = input(self.messages["msg_4"]) if msg_index == 10 else "y"
        if answer == "n":
            return self.memory
        elif answer == "y" and result.is_integer() and result < 10:
            answer = input(self.messages[f"msg_{msg_index}"])
        else:
            return result

        if answer == "n":
            return self.memory
        elif answer == "y" and msg_index < 12:
            return self.storage_confirmation(result, msg_index + 1)
        else:
            return result


    def should_result_be_stored(self, result):
        """After receiving the result, if the user wants to save the result in memory,
        the data is cleared and the memory field is filled with the obtained result.

        :param result: numeric value represents result of previous mathematical calculation
        :return: None (only changes instance fields)
        """
        self.memory = self.storage_confirmation(result)
        self.result = None
        self.number_one = None
        self.number_two = None
        self.operator = None

    def calculation(self):
        """Make the appropriate calculation and ask if the result should be stored for further use.
        
        :return: None
        """
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

    def is_one_digit(self):
        msg = ""
        if ((-10 < self.number_one < 10) and self.number_one.is_integer()
                and (-10 < self.number_two < 10) and self.number_two.is_integer()):
            msg += self.messages["msg_6"]

        return msg

    def is_val_one_and_multiply(self, msg: str):
        if (self.number_one == 1 or self.number_two == 1) and self.operator == "*":
            msg += self.messages["msg_7"]

        return msg

    def check_three(self, msg: str):
        if (self.number_one == 0 or self.number_two == 0) and self.operator in ("*", "+", "-"):
            msg += self.messages["msg_8"]
        return msg


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

            message = self.check_three(self.is_val_one_and_multiply(self.is_one_digit()))
            if message:
                print(self.messages["msg_9"] + message)


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
