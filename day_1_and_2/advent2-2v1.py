import copy


def is_increasing(levels, has_removed_already=False):
    for index in range(len(levels) - 1):
        if int(levels[index]) >= int(levels[index + 1]):
            if has_removed_already:
                return False, levels, has_removed_already
            else:
                copied_list_delete_first = copy.deepcopy(levels)
                del copied_list_delete_first[index]
                first_result = is_increasing(copied_list_delete_first, True)
                
                copied_list_delete_second = copy.deepcopy(levels)
                del copied_list_delete_second[index + 1]
                second_result = is_increasing(copied_list_delete_second, True)
                
                if first_result[0]:
                    return first_result
                elif second_result[0]:
                    return second_result
                else:
                    return False, [], has_removed_already
    return True, levels, has_removed_already

def is_decreasing(levels, has_removed_already=False):
    for index in range(len(levels) - 1):
        if int(levels[index]) <= int(levels[index + 1]):
            if has_removed_already:
                return False, levels, has_removed_already
            else:
                copied_list_delete_first = copy.deepcopy(levels)
                del copied_list_delete_first[index]
                first_result = is_decreasing(copied_list_delete_first, True)
                
                copied_list_delete_second = copy.deepcopy(levels)
                del copied_list_delete_second[index + 1]
                second_result = is_decreasing(copied_list_delete_second, True)
                
                if first_result[0]:
                    return first_result
                elif second_result[0]:
                    return second_result
                else:
                    return False, [], has_removed_already
    return True, levels, has_removed_already

def has_unacceptable_gap(levels, has_removed_already=False):
    for index in range(len(levels) - 1):
        first_number = int(levels[index])
        second_number = int(levels[index + 1])
        #print("FN:", first_number, "SN:",second_number)
        distance =  abs(second_number - first_number)
        #print(distance)
        if distance > 3:
            if has_removed_already:
                return True, levels, has_removed_already
            else:
                copied_list_delete_first = copy.deepcopy(levels)
                del copied_list_delete_first[index]
                first_result = has_unacceptable_gap(copied_list_delete_first, True)
                #print("First result:", first_result)
                
                copied_list_delete_second = copy.deepcopy(levels)
                del copied_list_delete_second[index + 1]
                second_result = has_unacceptable_gap(copied_list_delete_second, True)
                #print("Second result:", second_result)
                
                if not first_result[0]:
                    return first_result
                elif not second_result[0]:
                    return second_result
                else:
                    return True, [], has_removed_already
    return False, levels, has_removed_already

def unit_test():
    correct_list_increasing = ['4', '6', '8', '11', '14', '17', '18', '19']
    list_name = 'correct_list_increasing'
    #print(correct_list_increasing)
    
    result = is_increasing(correct_list_increasing)
    if result[0]:
        print(list_name + " correctly passed is_increasing")
    else:
        print(list_name + " incorrectly failed is_increasing")
    
    result = is_decreasing(correct_list_increasing)
    if result[0]:
        print(list_name + " incorrectly passed is_decreasing")
    else:
        print(list_name + " correctly failed is_decreasing")
        
    result = has_unacceptable_gap(correct_list_increasing)
    if result[0]:
        print(list_name + " incorrectly found gap too big")
    else:
        print(list_name + " correctly found no gaps")
    
    result = is_safe_report(correct_list_increasing)
    if result:
        print(list_name + " correctly passed is_safe_report")
    else:
        print(list_name + " incorrectly failed is_safe_report")
        
    #print(correct_list_increasing)
    
    
    correct_list_decreasing = ['10', '9', '8', '7', '6', '5', '4']
    list_name = 'correct_list_decreasing'
    result = is_increasing(correct_list_decreasing)
    if result[0]:
        print(list_name + " incorrectly passed is_increasing")
    else:
        print(list_name + " correctly failed is_increasing")
    
    result = is_decreasing(correct_list_decreasing)
    if result[0]:
        print(list_name + " correctly passed is_decreasing")
    else:
        print(list_name + " incorrectly failed is_decreasing")
        
    result = has_unacceptable_gap(correct_list_decreasing)
    if result[0]:
        print(list_name + " incorrectly found gap too big")
    else:
        print(list_name + " correctly found no gaps")
    
    result = is_safe_report(correct_list_decreasing)
    if result:
        print(list_name + " correctly passed is_safe_report")
    else:
        print(list_name + " incorrectly failed is_safe_report")
        
        
    incorrect_list_gap_double = ['15', '10', '5', '4', '3']
    list_name = 'incorrect_list_gap_double'
    
    result = is_increasing(incorrect_list_gap_double)
    if result[0]:
        print(list_name + " incorrectly passed is_increasing")
    else:
        print(list_name + " correctly failed is_increasing")
    
    result = is_decreasing(incorrect_list_gap_double)
    if result[0]:
        print(list_name + " correctly passed is_decreasing")
    else:
        print(list_name + " incorrectly failed is_decreasing")
        
    result = has_unacceptable_gap(incorrect_list_gap_double)
    if result[0]:
        print(list_name + " correctly found gap too big")
    else:
        print(list_name + " incorrectly found no gaps")
    
    result = is_safe_report(incorrect_list_gap_double)
    if result:
        print(list_name + " incorrectly passed is_safe_report")
    else:
        print(list_name + " correctly failed is_safe_report")
        
        
        
    correct_list_gap_single = ['15', '5', '4', '3']
    list_name = 'correct_list_gap_single'
    
    result = is_increasing(correct_list_gap_single)
    if result[0]:
        print(list_name + " incorrectly passed is_increasing")
    else:
        print(list_name + " correctly failed is_increasing")
    
    result = is_decreasing(correct_list_gap_single)
    if result[0]:
        print(list_name + " correctly passed is_decreasing")
    else:
        print(list_name + " incorrectly failed is_decreasing")
        
    result = has_unacceptable_gap(correct_list_gap_single)
    if result[0]:
        print(list_name + " incorrectly found gap too big")
    else:
        print(list_name + " correctly found no gaps")
    
    result = is_safe_report(correct_list_gap_single)
    if result:
        print(list_name + " correctly passed is_safe_report")
    else:
        print(list_name + " incorrectly failed is_safe_report")
        
        
    correct_decrease_with_single_raise = ['7', '8', '5', '4', '3']
    list_name = 'correct_decrease_with_single_raise'
    
    result = is_increasing(correct_decrease_with_single_raise)
    if result[0]:
        print(list_name + " incorrectly passed is_increasing")
    else:
        print(list_name + " correctly failed is_increasing")
    
    result = is_decreasing(correct_decrease_with_single_raise)
    if result[0]:
        print(list_name + " correctly passed is_decreasing")
    else:
        print(list_name + " incorrectly failed is_decreasing")
        
    result = has_unacceptable_gap(correct_decrease_with_single_raise)
    if result[0]:
        print(list_name + " incorrectly found gap too big")
    else:
        print(list_name + " correctly found no gaps")
    
    result = is_safe_report(correct_decrease_with_single_raise)
    if result:
        print(list_name + " correctly passed is_safe_report")
    else:
        print(list_name + " incorrectly failed is_safe_report")
        
        
    
    incorrect_decrease_with_double_raise = ['7', '8', '9', '6', '4', '3']
    list_name = 'incorrect_decrease_with_double_raise'
    
    result = is_increasing(incorrect_decrease_with_double_raise)
    if result[0]:
        print(list_name + " incorrectly passed is_increasing")
    else:
        print(list_name + " correctly failed is_increasing")
    
    result = is_decreasing(incorrect_decrease_with_double_raise)
    if result[0]:
        print(list_name + " incorrectly passed is_decreasing")
    else:
        print(list_name + " correctly failed is_decreasing")
        
    result = has_unacceptable_gap(incorrect_decrease_with_double_raise)
    if result[0]:
        print(list_name + " incorrectly found gap too big")
    else:
        print(list_name + " correctly found no gaps")
    
    result = is_safe_report(incorrect_decrease_with_double_raise)
    if result:
        print(list_name + " incorrectly passed is_safe_report")
    else:
        print(list_name + " correctly failed is_safe_report")
        
    
    
    correct_decreasing_must_delete_second = ['9', '8', '21' '7', '6', '5']
    list_name = 'correct_decreasing_must_delete_second'
    
    result = is_increasing(correct_decreasing_must_delete_second)
    if result[0]:
        print(list_name + " incorrectly passed is_increasing")
    else:
        print(list_name + " correctly failed is_increasing")
    
    result = is_decreasing(correct_decreasing_must_delete_second)
    if result[0]:
        print(list_name + " correctly passed is_decreasing")
    else:
        print(list_name + " incorrectly failed is_decreasing")
        
    result = has_unacceptable_gap(correct_decreasing_must_delete_second)
    if result[0]:
        print(list_name + " incorrectly found gap too big")
    else:
        print(list_name + " correctly found no gaps")
    
    result = is_safe_report(correct_decreasing_must_delete_second)
    if result:
        print(list_name + " correctly passed is_safe_report")
    else:
        print(list_name + " incorrectly failed is_safe_report")
        
        
    
    problem_one = ['79', '81', '77', '74', '72', '71', '70']
    list_name = 'problem_one'
    
    result = is_increasing(problem_one)
    if result[0]:
        print(list_name + " incorrectly passed is_increasing")
    else:
        print(list_name + " correctly failed is_increasing")
    
    result = is_decreasing(problem_one)
    if result[0]:
        print(list_name + " correctly passed is_decreasing")
    else:
        print(list_name + " incorrectly failed is_decreasing")
        
    result = has_unacceptable_gap(problem_one)
    if result[0]:
        print(list_name + " incorrectly found gap too big")
    else:
        print(list_name + " correctly found no gaps")
    
    result = is_safe_report(problem_one)
    if result:
        print(list_name + " correctly passed is_safe_report")
    else:
        print(list_name + " incorrectly failed is_safe_report")
    

def is_safe_report(levels):
    increasing, increasing_levels, has_removed_already_increasing = is_increasing(levels)
    decreasing, decreasing_levels, has_removed_already_decreasing = is_decreasing(levels)
    
    unacceptable_gap = True
    
    if increasing:
        unacceptable_gap, final_levels, has_removed_already_gap = has_unacceptable_gap(increasing_levels, has_removed_already_increasing)
        
    if decreasing:
        unacceptable_gap, final_levels, has_removed_already_gap = has_unacceptable_gap(decreasing_levels, has_removed_already_decreasing)

    print("Increasing:", increasing)
    print("Decreasing:", decreasing)
    print("Unacceptable gap:", unacceptable_gap)
    if (increasing or decreasing) and unacceptable_gap == False:
        return True
    else:
        #print(levels)
        return False
            



def calculate_safe_reports():
    safe_reports_count = 0

    with open('input2.txt', 'r') as file:
        lines = file.readlines()
        #print(lines)

        for line in lines:
            levels = line.strip()
            levels = levels.split()
            levels = [int(string) for string in levels] #convert to int
            #print(levels)        
            
            if is_safe_report(levels):
                safe_reports_count += 1
    print(safe_reports_count)






import copy

def is_increasing_original(levels):
    for index in range(len(levels) - 1):
        if int(levels[index]) >= int(levels[index + 1]):
            #print(levels[index], levels[index + 1])
            return False
    return True
def is_decreasing_original(levels):
    for index in range(len(levels) - 1):
        if int(levels[index]) <= int(levels[index + 1]):
            return False
    return True
def has_unacceptable_gap_original(levels):
    for index in range(len(levels) - 1):
        first_number = int(levels[index])
        second_number = int(levels[index + 1])
        #print("FN:", first_number, "SN:",second_number)
        distance =  abs(second_number - first_number)
        #print(distance)
        if distance > 3:
            return True
    return False

def unit_test_original():
    test_list = ['4', '5', '6', '7', '8', '16', '9']
    result = is_safe_report_remove_one(test_list)
    print(result)
            

def is_safe_report_remove_one(levels):
    increasing = is_increasing_original(levels)
    decreasing = is_decreasing_original(levels)
    unacceptable_gap = has_unacceptable_gap_original(levels)

    if (increasing or decreasing) and not unacceptable_gap:
        return True
    else:
        for index in range(len(levels)):
            copied_list = copy.deepcopy(levels)
            del copied_list[index]
            
            #print(copied_list)
            increasing = is_increasing_original(copied_list)
            #print(increasing)
            decreasing = is_decreasing_original(copied_list)
            #print(decreasing)
            unacceptable_gap = has_unacceptable_gap_original(copied_list)
            #print(unacceptable_gap)
            if (increasing or decreasing) and not unacceptable_gap:
                return True
    return False
    

def calculate_safe_reports_version_two():
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




def compare_safe_reports():
    with open('input2.txt', 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            levels = line.strip().split()
            result1 = is_safe_report(levels)
            result2 = is_safe_report_remove_one(levels)
            
            if result1 != result2:
                print(f"Levels: {levels}")
                print(f"is_safe_report: {result1}")
                print(f"is_safe_report_remove_one: {result2}")
                print("---")

#calculate_safe_reports()
#calculate_safe_reports_version_two()
unit_test()
#compare_safe_reports()
