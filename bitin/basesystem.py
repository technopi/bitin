class Base_Translation:
    def __init__(self, a, precision=5, d_type='decimal'):
        self.a = a
        self.d_type = d_type
        self.precision = precision

    def to_base(self, base):
        if self.d_type == 'decimal' and base != 1:
            integer_part = int(self.a)
            fractional_part = self.a - integer_part if isinstance(self.a, float) else 0.0
            integer_result = self.convert_integer_part(integer_part, base)
            fractional_result = self.convert_fractional_part(fractional_part, base)

            if fractional_result:
                return integer_result.fractional_result
            else:
                return integer_result
        else:
            raise ValueError('Error in selecting data_type or base for conversion')

    def convert_integer_part(self, number, base):
        integer_result = ''
        while number > 0:
            remainder = number % base
            integer_result = str(remainder) + integer_result
            number //= base
        return integer_result if integer_result else '0'

    def convert_fractional_part(self, number, base):
        fractional_result = ''
        while number > 0 and self.precision > 0:
            number *= base
            integer_part = int(number)
            fractional_result += str(integer_part)
            number -= integer_part
            self.precision -= 1
        return fractional_result

class BaseReversal:
    def __init__(self, number):
        self.number = number

    def from_base(self, base):
        decimal_number = int(str(self.number), base)
        return decimal_number
