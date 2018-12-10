use std::collections::HashMap;
use std::fs;

pub fn run() -> (i32, i32) {
    let contents = fs::read_to_string("input/1")
        .expect("Something went wrong reading the file");

    let mut non_repeating_frequency = 0;
    let mut frequencies = HashMap::new();
    let changes = contents.trim().split("\n");

    for change in changes {
        non_repeating_frequency += change.parse::<i32>().unwrap();
        frequencies.insert(non_repeating_frequency, 1);
    }

    let mut current_frequency = non_repeating_frequency;
    let mut changes = contents.trim().split("\n").cycle();

    while frequencies.get(&current_frequency) < Some(&2) {
        current_frequency += changes.next().unwrap().parse::<i32>().unwrap();
        if let Some(x) = frequencies.get_mut(&current_frequency) {
            *x += 1;
        }
    }
    (non_repeating_frequency, current_frequency)
}

#[cfg(test)]
mod part {
    use super::*;

    #[test]
    fn one_and_two() {
        assert_eq!(run(), (540, 73056));
    }
}
