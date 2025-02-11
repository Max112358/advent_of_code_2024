import copy

def is_increasing(levels):
    for index in range(len(levels) - 1):
        if int(levels[index]) >= int(levels[index + 1]):
            #print(levels[index], levels[index + 1])
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
    test_list = ['4', '5', '6', '7', '8', '16', '9']
    result = is_safe_report_remove_one(test_list)
    print(result)
    

def is_safe_report(levels):
    increasing = is_increasing(levels)
    decreasing = is_decreasing(levels)
    unacceptable_gap = has_unacceptable_gap(levels)

    if (increasing or decreasing) and not unacceptable_gap:
        return True
    else:
        return False
            

def is_safe_report_remove_one(levels):
    increasing = is_increasing(levels)
    decreasing = is_decreasing(levels)
    unacceptable_gap = has_unacceptable_gap(levels)

    if (increasing or decreasing) and not unacceptable_gap:
        return True
    else:
        for index in range(len(levels)):
            copied_list = copy.deepcopy(levels)
            del copied_list[index]
            
            #print(copied_list)
            increasing = is_increasing(copied_list)
            #print(increasing)
            decreasing = is_decreasing(copied_list)
            #print(decreasing)
            unacceptable_gap = has_unacceptable_gap(copied_list)
            #print(unacceptable_gap)
            if (increasing or decreasing) and not unacceptable_gap:
                return True
    return False
    

def calculate_safe_reports():
    safe_reports_count = 0

    with open('input2.txt', 'r') as file:
        lines = file.readlines()
        #print(lines)

        for line in lines:
            levels = line.strip() #remove \n
            levels = levels.split() #split by space
            levels = [int(string) for string in levels] #convert to int
            #print(levels)        
            
            if is_safe_report_remove_one(levels):
                safe_reports_count += 1
    print(safe_reports_count)

calculate_safe_reports()
#unit_test()