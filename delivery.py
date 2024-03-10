from typing import List


def min_transport_platforms(weights: List[int], limit: int) -> int:
    '''Функция определяет минимальное количество транспортных
    платформ, необходимое для перевозки всех роботов'''
    weights.sort()
    left, right = 0, len(weights) - 1
    platforms = 0

    while left <= right:
        if weights[left] + weights[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        platforms += 1

    return platforms


def main():
    weights = list(map(int, input("Введите веса роботов через пробел: ").split()))
    limit = int(input("Введите лимит веса на платформе: "))

    result = min_transport_platforms(weights, limit)
    print(f"Минимальное количество транспортных платформ: {result}")


if __name__ == "__main__":
    main()
