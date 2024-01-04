fn main() {
    println!("Hello, world!");
    for num in 1..=100 {
        match (num % 3, num % 5) {
            (0, 0) => println!("FizzBuzz"),
            (0, _) => println!("Fizz"),
            (_, 0) => println!("Buzz"),
            (_, _) => println!("{}", num),
        }
    }
}
