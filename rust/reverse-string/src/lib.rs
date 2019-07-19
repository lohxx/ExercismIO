pub fn reverse(input: &str) -> String {
    let mut reversed = String::new();
    for word in input.split_whitespace().rev(){
        reversed += word;
    }

    println!("{}", reversed);

    reversed
}
