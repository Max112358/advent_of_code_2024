def is_increasing(levels):
    for index in range(len(levels) - 1):
        if int(levels[index]) >= int(levels[index + 1]):
            print(levels[index], levels[index + 1])
            return False
    return True
def is_decreasing(levels):
    for index in range(len(levels) - 1):
        if int(levels[index]) <= int(levels[index + 1]):
            return False
    return True
def has_unacceptable_gap(levels):
    for index in range(len(levels) - 1):
        first_number = int(levels[index])
        second_number = int(levels[index + 1])
        #print("FN:", first_number, "SN:",second_number)
        distance =  abs(second_number - first_number)
        #print(distance)
        if distance > 3:
            return True
    return False

def unit_test():
    test_list = ['4', '6', '8', '11', '13', '16', '17', '19']
    result = is_increasing(test_list)
    print(result)

def is_safe_report(levels):
    increasing = is_increasing(levels)
    decreasing = is_decreasing(levels)
    unacceptable_gap = has_unacceptable_gap(levels)

    if increasing or decreasing:
        if unacceptable_gap:
            print("rejected UG: ", levels)
            return False
        else:
            return True
    else:
        print("rejected ID: ", levels)
        return False
            



def calculate_safe_reports():
    safe_reports_count = 0

    with open('input2.txt', 'r') as file:
        lines = file.readlines()
        #print(lines)

        for line in lines:
            levels = line.strip()
            levels = levels.split()

            for level in levels:
                level = int(level)
            #print(levels)        
            if is_safe_report(levels):
                safe_reports_count += 1
    print(safe_reports_count)

calculate_safe_reports()
#unit_test()