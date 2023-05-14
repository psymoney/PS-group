let fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');
const N = +input.shift()
const list = input.map(li => li.split(' ').map(Number))

list.sort((a,b) => a[1] - b[1] || a[0] - b[0])
let start = 0
let count = 0
for (let x of list) {
  if (start <= x[0]) {
    count += 1
    start = x[1]
  }
}
console.log(count)