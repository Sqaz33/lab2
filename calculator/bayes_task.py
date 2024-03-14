

class BayesTask:
    def calculate_probability(self, formulas_type: int, hypothesis_probab: list[float], conditional_probab: list[float]):
        match formulas_type:
            case 0:
                return self.total_probability(hypothesis_probab, conditional_probab)
            case 1:
                return self.bayes(hypothesis_probab, conditional_probab)

    def total_probability(self, hypothesis_probab: list[float], conditional_probab: list[float]) -> float:
        return sum(i * j for i, j in zip(hypothesis_probab, conditional_probab))

    def bayes(self, hypothesis_probab: list[float], conditional_probab: list[float]) -> list[float]:
        total = self.total_probability(hypothesis_probab, conditional_probab)
        return [i * j / total for i, j in zip(hypothesis_probab, conditional_probab)]
