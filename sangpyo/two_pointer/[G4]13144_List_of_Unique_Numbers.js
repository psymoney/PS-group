const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = +input.shift()
let A = input.shift().split(' ').map(Number)


const solution = () => {
  let answer = 0
  const set = new Set()

  let left = 0, right = 0
  while (right < N) {
    
    

    while (set.has(A[right])) {
      set.delete(A[left])
      left+=1
    }

    set.add(A[right])
    answer += (right - left) + 1

    right += 1
  }

  console.log(answer)
}

solution()
