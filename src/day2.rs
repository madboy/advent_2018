use std::collections::HashMap;
use std::fs;

pub fn run() -> (i32, String) {
    let contents = fs::read_to_string("input/2")
        .expect("Something went wrong reading the file");
    let box_ids = contents.trim().split("\n");
    let mut twos = 0;
    let mut threes = 0;

    for box_id in box_ids {
        let mut letters = HashMap::new();
        for l in box_id.chars() {
            let mut count = 1;
            if let Some(x) = letters.get(&l) {
                count = x + 1;
            }
            letters.insert(l, count);
        }

        let mut two_counted = false;
        let mut three_counted = false;
        for value in letters.values() {
            match value {
                &2 => {
                    if !two_counted {
                        twos += 1;
                        two_counted = true;
                    }
                },
                &3 => {
                    if !three_counted {
                        threes += 1;
                        three_counted = true;
                    }
                },
                &_ => (),
            }
        }
    }    
    (twos*threes, "a".to_string())
}

#[cfg(test)]
mod part {
    use super::*;

    #[test]
    fn one_and_two() {
        assert_eq!(run(), (7192, "mbruvapghxlzycbhmfqjonsie".to_string()));
    }
}
