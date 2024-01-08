import matplotlib.pyplot as plt
import numpy


class Function:
    k = 0
    m = 0
    n = 0


    def __init__(self, k, m, n) -> None:
        self.k = k
        self.m = m
        self.n = n

        # np.linspace() -> функція numpy, яка використовується для рівномірного розподілення n-кількості точок у інтервалі від k до m. 
        # У нашому випадку k i m -> -10 i 10, n -> 10 000.
        x = numpy.linspace(k, m, n)


        # Ініціалізація функції. Редагувати відповідно до потреб.
        y = x ** 2


        # Малюємо графік.
        self.draw_graph(x, y)


    def draw_graph(self, x, y):
        figure = plt.figure()


        # Додаємо осі для графіку.
        ax = figure.add_subplot(1, 1, 1)
        ax.spines['left'].set_position(('data', 0.0))
        ax.spines['bottom'].set_position(('data', 0.0))
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        # Власне графік. Тут plot -> графік, title -> назва графіку, grid -> сітка.
        plt.plot(x, y, color="red", label='f(x)=x^2')
        plt.title("Функція f(x)=x^2.")
        plt.grid(alpha=.4,linestyle='--')
        plt.show()


function = Function(-10, 10, 10_000)