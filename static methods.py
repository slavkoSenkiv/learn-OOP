# good if u need to organise functions together

class Math:

    @staticmethod
    def add5(x):
        x += 5
        return x

    @staticmethod
    def multiply_5(x):
        x *= 5
        return x

    def no_static_multiply_5(x):
        x *= 5
        return x


print(Math.add5(5))
print(Math.multiply_5(5))
print(Math.multiply_5(10))