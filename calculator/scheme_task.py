

class SchemeTask:
    def calculateProbability(self, q1, q2, q3, q4, q5):
        return (q1 + q4 - q1*q4) * q3 * (q2 + q5 - q2*q5)
