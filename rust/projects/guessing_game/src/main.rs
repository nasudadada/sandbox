use std::io;

fn main() {
    println!("Guess the number!");

    println!("Please input your guess!");

    let mut guess = String::new();

    io::stdin()
        .read_line(guess)
        .expect("Failed to readline");

    println!("You guessed: {}", guess);
}
