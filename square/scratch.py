import math as m


class SquareCalculations:
    def __init__(self):
        pass
    def calc_square_by_side(self, args):
        # args are string sides

        figure = None
        match args:
            case None:
                return TypeError("Value can't be None")
            case str():
                args = [float(i) for i in args.split(" ")]
                match len(args):
                    case 0:
                        return ValueError("Data is empty")
                    case 1:
                        r = args[0]
                        figure = "circle"
                        return round(m.pi * (r ** 2), 3)
                    case 2:
                        figure = "rectangle"
                        a, b = args
                        d = m.hypot(a, b)
                        return round(a * (m.sqrt((d ** 2) - (a ** 2))), 3)
                    case 3:
                        figure = "triangle"
                        a, b, c = args
                        argsCopy = args.copy()
                        hyp = max(argsCopy)
                        argsCopy.remove(hyp)
                        a1, b1 = argsCopy
                        # right triangle test
                        if round((a1 ** 2), 3) + round((b1 ** 2), 3) == round((hyp ** 2), 3):
                            figure = "right triangle"
                            return (a1 * b1) / 2
                        else:
                            ph = (a + b + c) / 2
                            return round(m.sqrt(ph * (ph - a) * (ph - b) * (ph - c)), 3)
            case _:
                return TypeError("Unsupported data type")
