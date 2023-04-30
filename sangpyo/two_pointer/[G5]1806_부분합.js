const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, target] = input.shift().split(' ').map(Number)
const list = input[0].split(' ').map(Number)

const table = []
table[0] = list[0]
let startIndex = 0
let answer = Infinity
for (let i = 1; i < N; i++) {
  table[i] = list[i] + table[i - 1]
  if (table[i] >= target) {
    answer = Math.min(answer, i+1)
  }
}

for (startIndex; startIndex < N; startIndex++) {
  const cur = table[startIndex]


  for (let j = startIndex; j >= 0; j--) {
    const prev = table[j]
    const prefix = cur - prev
    if (prefix >= target) {
      if (answer > startIndex - j) {
        answer = startIndex - j
      } else {
        break;
      }
    }
  }
  if (cur >= target) {
    answer = Math.min(answer, startIndex+1)
  }
}
console.log(answer > N ? 0 : answer)
