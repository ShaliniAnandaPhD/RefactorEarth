def find_duplicates(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    return duplicates

items = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1]
duplicate_items = find_duplicates(items)
