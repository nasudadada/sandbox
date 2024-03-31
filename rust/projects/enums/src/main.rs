enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

impl Message {
    fn call(&self) {
        match self {
            Message::Quit => println!("Quit"),
            Message::Move { x, y } => println!("Move to x: {}, y: {}", x, y),
            Message::Write(text) => println!("Write: {}", text),
            Message::ChangeColor(r, g, b) => {
                println!("Change color to R: {}, G: {}, B: {}", r, g, b)
            }
        }
    }
}

fn main() {
    let m1 = Message::Quit;
    m1.call();

    let m2 = Message::Move { x: 2, y: 4 };
    m2.call();

    let m3 = Message::Write(String::from("hello"));
    m3.call();

    let m4 = Message::ChangeColor(255, 0, 0);
    m4.call()
}
