struct User {
    username: String,
    email: String,
    sign_in_count: u64,
    active: bool,
}

fn main() {
    let user1 = User{
        username: String::from("somethinger"),
        email: String::from("something@example.com"),
        sign_in_count: 1,
        active: true,
    };
    println!("{}", user1.username);
}
