const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M] = input.shift().split(' ').map(Number)
let A = input.map(Number)


const solution = () => {
  let answer = Infinity

  A.sort((a, b) => a - b)

  let left = 0, right = 0
  while (left < N && right < N) {
    const sum = Math.abs(A[left] - A[right])

    if (sum === M) {
      answer = Math.min(sum, answer)
      break
    }
    
    if (sum > M) {
      answer = Math.min(sum, answer)
      right += 1
    } else {
      left += 1
    }
  }

  console.log(answer)
}

solution()