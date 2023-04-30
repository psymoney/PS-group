let fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const len = +input.shift();
let data = input[0].split(' ').map(Number);

data.sort((a, b) => a - b)

let left = 0, right = len-1
let prevAbs = Math.abs(data[left] + data[right])
let answer = [data[left], data[right]]

while (left < right) {
  const sum = data[left] + data[right]
  const abs = Math.abs(data[left] + data[right])

  if (sum === 0) return console.log(`${data[left]} ${data[right]}`)
  else if (prevAbs > abs) {
    prevAbs = abs
    answer = [data[left], data[right]]
  }

  if (sum < 0) {
    left += 1
  } else {
    right -= 1
  }
}

console.log(answer.join(' '))