class ComplexNumbers:

    def __init__(self, complex_n):
        self.complex_n = complex_n

    def __add__(self, other):
        new_real = self.complex_n[0] + other.complex_n[0]
        new_imaginary = self.complex_n[1] + other.complex_n[1]
        return ComplexNumbers((new_real, new_imaginary))

    def __sub__(self, other):
        new_real = self.complex_n[0] - other.complex_n[0]
        new_imaginary = self.complex_n[1] - other.complex_n[1]
        return ComplexNumbers((new_real, new_imaginary))

    def __mul__(self, other):
        new_real = self.complex_n[0] * other.complex_n[0] - self.complex_n[1] * other.complex_n[1]
        new_imaginary = self.complex_n[0] * other.complex_n[1] + self.complex_n[1] * other.complex_n[0]
        return ComplexNumbers((new_real, new_imaginary))

    def __truediv__(self, other):
        new_real = (self.complex_n[0] * other.complex_n[0] + self.complex_n[1] * other.complex_n[1]) / \
                   (other.complex_n[0] * other.complex_n[0] + other.complex_n[1] * other.complex_n[1])
        new_imaginary = (self.complex_n[1] * other.complex_n[0] - self.complex_n[0] * other.complex_n[1]) / \
                        (other.complex_n[0] * other.complex_n[0] + other.complex_n[1] * other.complex_n[1])
        return ComplexNumbers((new_real, new_imaginary))

    def getter(self):
        if self.complex_n[1] < 0:
            real_string = str(self.complex_n[0])
            imaginary_string = str(self.complex_n[1])
            return real_string[:4] + imaginary_string[:4] + 'i'
        else:
            real_string = str(self.complex_n[0])
            imaginary_string = str(self.complex_n[1])
            return real_string[:4] + '+' + imaginary_string[:4] + 'i'


real_part1 = 10
imaginary_part1 = -4

real_part2 = 5
imaginary_part2 = 1

complex_number_a = ComplexNumbers((real_part1, imaginary_part1))
complex_number_b = ComplexNumbers((real_part2, imaginary_part2))

result = complex_number_a + complex_number_b
print(f"{complex_number_a.getter()} + {complex_number_b.getter()} = {result.getter()}")

result = complex_number_a - complex_number_b
print(f"{complex_number_a.getter()} - {complex_number_b.getter()} = {result.getter()}")

result = complex_number_a * complex_number_b
print(f"{complex_number_a.getter()} * {complex_number_b.getter()} = {result.getter()}")

result = complex_number_a / complex_number_b
print(f"{complex_number_a.getter()} / {complex_number_b.getter()} = {result.getter()}")

