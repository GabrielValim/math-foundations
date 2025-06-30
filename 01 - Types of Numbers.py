from fractions import Fraction
from typing import List
import math


class Number:
    def __init__(self, value: str) -> None:
        try:
            self.value = float(value)
        except ValueError:
            raise ValueError(f"Invalid value: {value}")

    def is_real(self) -> bool:
        return math.isfinite(self.value)

    def is_natural(self) -> bool:
        return self.is_real() and self.value.is_integer() and self.value >= 0

    def is_integer(self) -> bool:
        return self.is_real() and self.value.is_integer()

    def is_rational(self) -> bool:
        if not self.is_real():
            return False
        try:
            fraction = Fraction(self.value).limit_denominator()
            return float(fraction) == self.value
        except Exception:
            return False

    def is_irrational(self) -> bool:
        return self.is_real() and not self.is_rational()


class NumberClassifier:
    def __init__(self, number: Number):
        self.number = number

    def classify(self) -> List[str]:
        if not self.number.is_real():
            return ["Not a real number"]

        sets: List[str] = []

        if self.number.is_natural():
            sets.append("ℕ (Natural)")
        if self.number.is_integer():
            sets.append("ℤ (Integer)")
        if self.number.is_rational():
            sets.append("ℚ (Rational)")
        if self.number.is_irrational():
            sets.append("I (Irrational)")

        sets.append("ℝ (Real)")
        return sets


if __name__ == "__main__":
    value: str = input("Enter a number: ")

    try:
        number = Number(value=value)
        classifier = NumberClassifier(number)
        print(
            f"The number {number.value} belongs to: {', '.join(classifier.classify())}"
        )
    except ValueError as e:
        print(e)
