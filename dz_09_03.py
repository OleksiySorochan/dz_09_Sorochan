# Я так зрозумів, що параметр length - це довжина паролілограма , а не довжина сторони.
# A width  - це ширина, топто висота. Також сказано що одна діагональ перпендікулярна стороні,
# а це значить що паролілограм утворюється двома, прямоугольними рівнобеденними трикутниками.
# Як що продовжити базову сторону до дліни і провести перпендікуляри до вершин,
# то утвориться прямокутник, який складається із паролілограмма і двох прямокутник трикутниках.
# Із відомою вище інформаціі робимо вивод що площа двох доповнених трикутників равна половині площі паролілограмма. Sпрям = (Sпар + Sтрик * 2).
# Тобто формула для данного паролілограмма - s_pal = (l * w) / 3 * 2
class Paralilogram:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        w = self.width
        l = self.length
        s_pal = (l * w) / 3 * 2
        return s_pal

class Square(Paralilogram):
    def get_area(self):
        w = self.width
        l = self.length
        s_sq = w * l
        return s_sq

pal = Paralilogram(25, 6)
print(pal.get_area())
sq = Square(5,5)
print(sq.get_area())

#Варіант 2 як що length - це сторона, а width - це висота

class Paralilogram2:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        w = self.width
        l = self.length
        return l * w

class Square2(Paralilogram2):
    def __init__(self, a):
        self.a = a

    def get_area(self):
        return self.a ** 2


pal2 = Paralilogram2(12, 34)
print(pal2.get_area())
sq2 = Square2(5)
print(sq2.get_area())