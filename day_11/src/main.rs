use lazy_static::lazy_static;
use std::collections::HashMap;
use std::sync::{Arc, Mutex};
use std::thread; // This import is necessary for creating threads

lazy_static! {
    static ref memoization: Arc<Mutex<HashMap<(String, u64), u64>>> =
        Arc::new(Mutex::new(HashMap::new()));
}

fn check_and_get_from_dict(key: &(String, u64)) -> Option<u64> {
    // Lock the mutex and access the HashMap
    let dict = memoization.lock().unwrap();

    // Check if the key exists and return the value if it does
    dict.get(key).cloned() // `.cloned()` is used to return the value by value (not reference)
}

fn insert_into_dict(key: (String, u64), value: u64) {
    let mut dict = memoization.lock().unwrap();
    dict.insert(key, value);
}

fn main() {
    println!("Hello, worlds!");
    //recursive_loop(5); // Start the recursion with count = 5

    //let numbers = vec![0, 1, 10, 99, 999]; // Creates a vector with initial values
    //let numbers = vec![125, 17]; // Creates a vector with initial values
    //let numbers = vec![890, 0, 1, 935698, 68001, 3441397, 7221, 27]; // Creates a vector with initial values

    let numbers = vec![890, 0, 1, 935698, 68001, 3441397, 7221, 27]; // Creates a vector with initial values

    println!("{:?}", numbers); // Output: [1, 2, 3, 4, 5]

    let num_blinks = 75;

    let mut handles = vec![]; // Vector to hold thread handles

    // Loop over the array and create a thread for each element
    for &element in &numbers {
        let handle = thread::spawn(move || {
            // Perform some operation for each element
            println!("Thread processing element: {}", element);
            let result = get_expanded_length(element.to_string(), num_blinks);
            result // Return the result from the thread
        });
        handles.push(handle); // Collect the thread handle
    }

    let mut results = vec![];
    for handle in handles {
        results.push(handle.join().unwrap()); // Collect returned values
    }

    let total: u64 = results.iter().sum();

    println!("answer: {:?}", total); // Output the numbers
}

fn get_expanded_length(input: String, blinks_remaining: u64) -> u64 {
    if blinks_remaining == 0 {
        //println!("input: {}", input);
        return 1;
    } else {
        let key = (input.clone(), blinks_remaining);

        match check_and_get_from_dict(&key) {
            Some(value) => {
                return value;
            }
            None => {
                // If the key is not found, just continue the execution
                // You can leave this block empty or log a message if needed
            }
        }

        if input.clone() == "0" {
            let length = get_expanded_length("1".to_string(), blinks_remaining - 1);
            insert_into_dict(key.clone(), length);
            return length;
        } else if input.len() % 2 == 0 {
            let first_string = input[0..input.len() / 2].to_string();
            let second_string = input[input.len() / 2..].to_string();

            let first_to_num = first_string.parse::<u64>().unwrap();
            let second_to_num = second_string.parse::<u64>().unwrap();

            let first_back_to_string = (first_to_num).to_string();
            let second_back_to_string = (second_to_num).to_string();

            let first_length = get_expanded_length(first_back_to_string, blinks_remaining - 1);
            let second_length = get_expanded_length(second_back_to_string, blinks_remaining - 1);
            let combined_length = first_length + second_length;

            insert_into_dict(key.clone(), combined_length);
            return combined_length;
        } else {
            let num: u64 = input.parse().expect("Not a valid number");
            let num_multiplied = num * 2024;
            let length = get_expanded_length(num_multiplied.to_string(), blinks_remaining - 1);

            insert_into_dict(key.clone(), length);
            return length;
        }
    }
}
