def delete_nth(order,max_e):
    result = []
    occurrences = {}
    for element in order:
        occurrences[element] = occurrences.get(element, 0) + 1
        if occurrences[element] <= max_e:
            result.append(element)

    return result
