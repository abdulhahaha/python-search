def binary_search_definition(dict, target_word):
    left = 0
    right = len(dict) - 1

    while left <= right:
        mid = (left + right) // 2

        if dict[mid][0] == target_word:
            return dict[mid][1]
        elif dict[mid][0] < target_word:
            left = mid + 1
        else:
            right = mid - 1

    return "Definisi kata tidak ditemukan."

dict = [
    ["Apple", "Buah Apel"],
    ["Banana", "Buah Pisang"],
    ["Cat", "Kucing"],
    ["Duck", "Bebek"],
    ["Elephant", "Gajah"]
]

target_word = "Cat"

definition = binary_search_definition(dict, target_word)
if definition != "Definisi kata tidak ditemukan.":
    print("Definisi kata", target_word + ":", definition)
else:
    print(definition)