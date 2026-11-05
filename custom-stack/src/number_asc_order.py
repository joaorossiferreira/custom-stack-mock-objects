from src.custom_stack_class import CustomStack


class NumberAscOrder:
    """Coleta os numeros sorteados da Mega Sena armazenados em uma CustomStack
    e os retorna em uma lista ordenada de forma ascendente."""

    def sort(self, stack):
        if stack is None:
            raise ValueError("A pilha nao pode ser None")
        if not isinstance(stack, CustomStack):
            raise TypeError("O parametro deve ser uma CustomStack")

        numbers = []
        while not stack.is_empty():
            number = stack.pop()
            if isinstance(number, bool) or not isinstance(number, int):
                raise TypeError("A pilha deve conter apenas numeros inteiros")
            numbers.append(number)

        return sorted(numbers)
