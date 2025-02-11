def calculate_similarity_score():
    list1 = []
    list2 = []
    similarity_score = 0

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

    count_map = {}
    for number in list2:
        if number in count_map:
            count_map[number] += 1
        else:
            count_map[number] = 1

    for number in list1:
        if number in count_map:
            similarity_score += number * count_map[number]
    print(similarity_score)

calculate_similarity_score()