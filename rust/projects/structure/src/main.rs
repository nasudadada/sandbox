struct User {
    username: String,
    email: String,
    sign_in_count: u64,
    active: bool,
}

struct Color(i32, i32, i32);
struct Point(i32, i32, i32);


fn main() {
    let user1 = User{
        username: String::from("somethinger"),
        email: String::from("something@example.com"),
        sign_in_count: 1,
        active: true,
    };
    println!("{}", user1.username);

    let black = Color(0, 0, 0);
    println!("{}", black.0);
    let origin = Point(0, 0, 0);
}
