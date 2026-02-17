def is_same_data_type(items: list):
    for item in range(len(items)):
        if type(items[0]) == type(items[item]):
            continue
        else:
            return False
    return True
print(is_same_data_type([]))