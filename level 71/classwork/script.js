let num = parseInt(prompt("Enter a number"))
let sum = 0

for (let i = 1; i <= num; i++) {
    if (i % 2 == 0) {
        sum += i
    }
}
console.log(sum)
