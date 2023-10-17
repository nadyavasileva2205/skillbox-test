def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Пример использования
original_list = [1, 4, -3, 0, 10]

print("Изначальный список:", original_list)
bubble_sort(original_list)
print("Отсортированный список:", original_list)