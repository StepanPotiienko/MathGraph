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

        functions_dictionary = {"x**2": x**2, "x**3": x**3, "sqrt(x)": x**0.5}
        print("Available functions: ", functions_dictionary.keys())

        # Ініціалізація функції. Редагувати відповідно до потреб.
        function_number = int(
            input(
                "Please choose the number of the function you want to graph: (0 - "
                + str(len(functions_dictionary) - 1)
                + "): "
            )
        )
        # Малюємо графік.
        self.draw_graph(
            x,
            list(functions_dictionary.values())[function_number],
            label=list(functions_dictionary.keys())[function_number],
        )

    def draw_graph(self, x, y, label):
        figure = plt.figure()

        # Додаємо осі для графіку.
        ax = figure.add_subplot(1, 1, 1)
        ax.spines["left"].set_position(("data", 0.0))
        ax.spines["bottom"].set_position(("data", 0.0))
        ax.spines["right"].set_color("none")
        ax.spines["top"].set_color("none")

        # Власне графік. Тут plot -> графік, title -> назва графіку, grid -> сітка.
        plt.plot(x, y, color="red")
        plt.title("Функція f(x)={label}.".format(label=label))
        plt.grid(alpha=0.4, linestyle="--")
        plt.show()


function = Function(-10, 10, 10_000)
