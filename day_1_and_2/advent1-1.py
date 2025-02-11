def calculate_total_distance():
    list1 = []
    list2 = []
    total_distance = 0

    with open('input.txt', 'r') as file:
        lines = file.readlines()
        #print(lines)

    for line in lines:
        parts = line.split('   ')
        #print(parts)
        parts_of_second_numbers = parts[1].split('\n')
        #print(parts_of_second_numbers)
        parts[0] = int(parts[0])
        parts_of_second_numbers[0] = int(parts_of_second_numbers[0])
        list1.append(parts[0])
        list2.append(parts_of_second_numbers[0])
    list1.sort()
    list2.sort()

    for index, number in enumerate(list1):
        total_distance += abs(number - list2[index])

    print(total_distance)




calculate_total_distance()