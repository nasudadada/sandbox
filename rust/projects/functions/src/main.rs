fn main() {
    println!("Hello, world!");
    another_function(5);
    print_labeled_measurement(5, 'h');
    let x = seven();

    println!("The value of x is: {}", x);
}

fn another_function(x: i32) {
    println!("The value of x is: {}", x); // xの値は{}です
}

fn print_labeled_measurement(value: i32, unit_label: char) {
    println!("The measurement is: {}{}", value, unit_label);
}

fn seven() -> i32 {
    7 // ;で閉じてないのでこれは式になり、暗黙的に返される
}
