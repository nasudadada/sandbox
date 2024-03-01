fn main() {
    let x = 5;

    let x = x + 1;
    {
        let x = x * 2;

        println!("The value of x in the inner scope is: {}", x);
    }
    println!("The value of x is: {}", x);

    let guess: u32 = "42".parse().expect("Not a Number");

    /* 数値演算 */
    // 足し算
    let sum = 5 + 10;
    println!("The value of sum is: {}", sum);

    // 引き算
    let difference = 95.5 - 4.3;
    // let difference = 895.5 - 754.1; -> 141.39999999999998 why?
    println!("The value of difference is: {}", difference); // 91.2

    // 掛け算
    let product = 4.0 * 30.0; // integerとfloatとかにすると動かない
    println!("The value of product is: {}", product); // 結果は整数で出力される

    // 割り算
    let quotient = 56.7 / 32.2;
    println!("The value of quotient is: {}", quotient); //
    let floored = 2 / 3;
    println!("The value of floored is: {}", floored); // 0 切り捨て？
    
    // 余り
    let remainder = 43 % 5;
    println!("The value of remainder is: {}", remainder);

    /* 論理値型 */
    let t = true;
    println!("The value of t is: {}", t);
    let f:bool = false; // 明示的な型注釈
    println!("The value of f is: {}", f);


    /* 文字型 文字列とは違うみたい */
    let c = 'z';
    let z = 'ℤ';
    let heart_eyed_cat = '😻';    //ハート目の猫
    println!("The value of c: {}, z:{}, heart_eyed_cat:{}",c,z,heart_eyed_cat)

    /* 複合型 */
    let tup:(i32, f64, u8) = (500, 6.4, 1)
}
