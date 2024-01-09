function fizzBuzz(max: number): void {
    for (let i = 1; i <= max; i++) {
        let output = '';

        if (i % 3 === 0) {
            output += 'Fizz';
        }
        if (i % 5 === 0) {
            output += 'Buzz';
        }

        console.log(output || i);
    }
}

fizzBuzz(100);
