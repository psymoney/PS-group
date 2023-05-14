const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M] = input.shift().split(' ').map(Number)
let A = input.map(Number)

// O(logM * M)
const solution = () => {
  const answer = binarySearch(A)
  
  console.log(answer)

  // O(log M)
  function binarySearch(arr) {
    
    // 0개씩 나눠 주거나, 다 나눠주거나
    let left = 0, right = 0
    for (let x of arr) right = Math.max(right, x)

    while (left < right) {
      const mid = (right + left) >>> 1

      const res = split(mid)

      if (res) {
        right = mid
      } else {
        left = mid + 1
      }
    }

    // O(M)
    // 아이들에게 나눠주기
    function split(mid) {
      let res = 0
      for (let x of arr) {
        res += Math.ceil(x / mid)
      }
      return res <= N
    }

    return left
  }

}

solution()

