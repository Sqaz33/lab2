

class SchemeTask:
    def calculateProbability(self, q1, q2, q3, q4, q5):
        return (q1 + q4 - q1*q4) * q3 * (q2 + q5 - q2*q5)


if __name__ == '__main__':
    st = SchemeTask()
    print(st.calculateProbability(1, 0.2, 0.3, 0.1, 1))
