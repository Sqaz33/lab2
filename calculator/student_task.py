from math import factorial as fact


def C(k: int, n: int):
    return fact(n) // (fact(n - k) * fact(k))


class StudentTask:
    def calculate_probability(self, formulas_type: int, m1: int, m2: int, n: int) -> tuple[list[float], float]:
        prom = [self.f1(m1, n), self.f2(m1, n), self.f3(m1, n), self.f4(m1, n),
                self.g1(m2, n), self.g1(m2, n), self.g1(m2, n), self.g1(m2, n)]
        answer = 0.0
        match formulas_type:
            case 0:
                answer = self.both_students(m1, m2, n)
            case 1:
                answer = self.only_firth_student(m1, m2, n)
            case 2:
                answer = self.only_one_student(m1, m2, n)
            case 3:
                answer = self.at_least_one_student(m1, m2, n)

        return prom, answer

    def f1(self, m1, n) -> float:
        return C(3, m1) / C(3, n)

    def f2(self, m1, n) -> float:
        return C(2, m1) * C(1, n - m1) / C(3, n)

    def f3(self, m1, n) -> float:
        return C(1, m1) * C(2, n - m1) / C(3, n)

    def f4(self, m1, n) -> float:
        return C(3, n - m1) / C(3, n)

    def g1(self, m2, n) -> float:
        return C(3, m2) / C(3, n)

    def g2(self, m2, n) -> float:
        return C(2, m2) * C(1, n - m2) / C(3, n)

    def g3(self, m2, n) -> float:
        return C(1, m2) * C(2, n - m2) / C(3, n)

    def g4(self, m2, n) -> float:
        return C(3, n - m2) / C(3, n)

    def both_students(self, m1: int, m2: int, n: int) -> float:
        return ((C(2, m1) * C(1, n - m1) / C(3, n)) * (C(2, m2) * C(1, n - m2) / C(3, n))
                + (C(3, m1) / C(3, n)) * (C(2, m2) * C(1, n - m2)) / C(3, n)
                + (C(3, m2) / C(3, n)) * (C(2, m1) * C(1, n - m1) / C(3, n))
                + (C(3, m2) / C(3, n)) * (C(3, m1) / C(3, n)))

    def only_firth_student(self, m1: int, m2: int, n: int) -> float:
        return ((C(2, m1) * C(1, n - m1) / C(3, n)) * (C(3, n - m2) / C(3, n))
                + (C(3, m1) / C(3, n)) * (C(3, n - m2) / C(3, n))
                + (C(1, m2) * C(2, n - m2) / C(3, n)) * (C(2, m1) * C(1, n - m1) / C(3, n))
                + (C(1, m2) * C(2, n - m2) / C(3, n)) * (C(3, m1) / C(3, n)))

    def only_one_student(self, m1: int, m2: int, n: int) -> float:
        return self.only_firth_student(m1, m2, n) + self.only_firth_student(m2, m1, n)

    def at_least_one_student(self, m1: int, m2: int, n: int) -> float:
        return self.only_one_student(m1, m2, n) + self.both_students(m1, m2, n)
