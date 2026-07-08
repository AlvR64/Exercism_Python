class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        # 1. Quitamos espacios
        number = self.card_num.replace(" ", "")

        # 2. Si tiene longitud 1 o menos, no es válido
        if len(number) <= 1:
            return False

        # 3. Si contiene algo que no sea dígito, no es válido
        if not number.isdigit():
            return False

        # 4. Convertimos a lista de ints
        digits = [int(digit) for digit in number]

        # 5. Recorremos desde la derecha
        total = 0
        should_double = False

        for digit in reversed(digits):
            if should_double:
                digit *= 2

                if digit > 9:
                    digit -= 9

            total += digit
            should_double = not should_double

        # 6. Es válido si la suma es divisible entre 10
        return total % 10 == 0