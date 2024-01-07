print("======================")
print("MUHAMMAD GALUH GUMELAR")
print("======================")

print("Sequential Search")
def sequentialsearch(data, value):
    index = []
    for i in range(len(data)):
        if data[i] == value:
            index.append(i)
    return index

def lebihBesar(data, value):
    index = []
    for i in range(len(data)):
        if data[i] > value:
            index.append(i)
    return index

data = [47,43,25,87,39,59,45,67,83,92,67]
x = 59

a = sequentialsearch(data, x)
b = lebihBesar(data, x)

print(data)
print("Nilai yang sama dengan {} berada pada indeks ke: {}".format(x, a))
print("Nilai yang lebih besar dari {} berada pada indeks ke: {}".format(x, b))

print("\n===================================================================\n")











print("Binary Search")
def binarySearch(data, value):
    first = 0
    last = len(data) - 1
    index = []
    while first <= last:
        midpoint = (first + last) // 2
        if data[midpoint] == value:
            index.append(midpoint)
            i = midpoint - 1
            while i >= 0 and data[i] == value:
                index.append(i)
                i -= 1
            i = midpoint + 1
            while i < len(data) and data[i] == value:
                index.append(i)
                i += 1
            return index
        else:
            if value < data[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return index

def sortData(data):
    for i in range(len(data)):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]    
    return data

def nilaisama(data, value):
    sorted_data = sortData(data)
    return binarySearch(sorted_data, value)


def lebihbesar(data, value):
    sorted_data = sortData(data)
    result = []
    for i in range(len(sorted_data)):
        if sorted_data[i] > value:
            result.append(i)
    return result

data = [47,43,25,87,39,59,45,67,83,92,67]
x = 59
print(sortData(data))
print(f"Nilai yang sama dengan {x} berada pada indeks ke: {nilaisama(data, x)}")
print(f"Nilai yang lebih besar dari {x} berada pada indeks ke: {lebihbesar(data, x)}")

