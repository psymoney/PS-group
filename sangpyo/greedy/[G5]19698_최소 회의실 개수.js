const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n"); 
// -------------------------------------------

const solution = () => {
  const N = +input.shift()
  const list = input.map(l => l.split(' ').map(Number))

  const arr = []
  for (let [s, e] of list) {
    arr.push([s, 1])
    arr.push([e, -1])
  }

  let answer = 0, count = 0

  arr.sort((a,b) => a[0] - b[0] || a[1] - b[1])

  for (let [a, b] of arr) {
    count += b
    answer = Math.max(answer, count)
  }

  console.log(answer);
}

solution()