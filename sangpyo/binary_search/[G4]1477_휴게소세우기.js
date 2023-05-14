const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M, L] = input.shift().split(' ').map(Number)
// N이 0일수도
let arr = []
if (N !== 0) arr = input.shift().split(' ').map(Number)

// O(logL * N)
const solution = () => {
  arr.push(L)
  arr.sort((a, b) => a - b) // 오름차순
  
  const answer = binarySearch()
  
  console.log(answer)

  // O(log L)
  function binarySearch() {
    let left = 0, right = L

    while (left < right) {
      const mid = (right + left) >>> 1

      const res = build(mid)

      if (res <= M) {
        right = mid
      } else {
        left = mid + 1
      }
    }

    // O(N)
    function build(mid) {
      let res = 0, prev = 0

      for (let x of arr) {
        const dist = x - prev

        if (dist > mid) {
          res += Math.ceil(dist / mid) -1
        }

        prev = x
      }

      res += Math.floor((L - prev) / mid)

      return res
    }

    return left
  }
}

solution()
