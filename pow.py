class PowerCalculator:
    def my_pow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2

        return result

# Example usage:
calculator = PowerCalculator()
base = 2
exponent = 5
result = calculator.my_pow(base, exponent)
print(f"The result of {base} raised to the power of {exponent} is: {result}")
