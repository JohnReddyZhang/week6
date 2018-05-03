import unittest

class PrimeFactors:

    def generate(n):
        factors = []
        divisor = 2
        while n > 1:
            while n % divisor == 0:
                factors.append(divisor)
                n = n / divisor
            divisor += 1
        return factors

class FactoringTests(unittest.TestCase):

    def test_factoring(self):
        assert [] == PrimeFactors.generate(1)
        assert [2] == PrimeFactors.generate(2)
        assert [3] == PrimeFactors.generate(3)
        assert [2,2] == PrimeFactors.generate(4)
        assert [5] == PrimeFactors.generate(5)
        assert [2,3] == PrimeFactors.generate(6)
        assert [7] == PrimeFactors.generate(7)
        assert [2,2,2] == PrimeFactors.generate(8)
        assert [3,3] == PrimeFactors.generate(9)
        assert [2,3,5,7] == PrimeFactors.generate(210)

if __name__ == '__main__':
    unittest.main()
