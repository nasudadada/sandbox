// 摂氏から華氏への変換関数
fn celsius_to_fahrenheit(celsius: f64) -> f64 {
    // 摂氏を華氏に変換する式
    celsius * 9.0 / 5.0 + 32.0
}

// 華氏から摂氏への変換関数
fn fahrenheit_to_celsius(fahrenheit: f64) -> f64 {
    // 華氏を摂氏に変換する式
    (fahrenheit - 32.0) * 5.0 / 9.0
}

fn main() {
    // 摂氏から華氏への変換
    let celsius = 25.0;
    let fahrenheit = celsius_to_fahrenheit(celsius);
    println!("{}°C is {}°F", celsius, fahrenheit);

    // 華氏から摂氏への変換
    let fahrenheit = 77.0;
    let celsius = fahrenheit_to_celsius(fahrenheit);
    println!("{}°F is {}°C", fahrenheit, celsius);
}