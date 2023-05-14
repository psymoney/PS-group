const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M] = input.shift().split(' ').map(BigInt)
let A = input.map(Number)


const solution = () => {
  const bigInt = binarySearch()
  
  console.log(bigInt.toString())

  // log N
  function binarySearch() {
    // T의 최고값 10^9, M의 최고값 10^9 => 최대 10^18
    let left = 0n, right = 1000000000000000000n

    while (left < right) {
      const mid = (right + left) / 2n

      const res = isPossible(mid)
      
      if (res) {
        right = mid
      } else {
        left = mid + 1n
      }
    }

    return left
  }

  // N
  // 심사관 한명이 제한시간 내에 몇명을 처리하는지 계산 * 모든 심사관 === 제한시간에 모든 심사관들이 처리할 수 있는 승객 수
  function isPossible(limitTime) {
    let acceptedPerson = 0n

    for (let inspector of A) {
      acceptedPerson += limitTime / BigInt(inspector)

      if (acceptedPerson >= M) return true
    }
    
    return acceptedPerson >= M
  }
}

solution()