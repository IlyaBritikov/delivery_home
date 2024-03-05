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


# Чтение входных данных
weights = list(map(int, input().split()))
limit = int(input())

# Вызов функции и вывод результата
print(min_transport_platforms(weights, limit))