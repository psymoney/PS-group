const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, K] = input.shift().split(' ').map(Number);
const list = input.shift().split(' ').map(Number);

// 슬라이딩 윈동
// 슬라이딩 크기에서 사용된 k개 빼기

let left = 0, right = 0, answer = 0, remove = K

for (right; right < N; right++) {
  const R = list[right]

  if (R % 2 !== 0) {
    remove -= 1
  }

  while (remove < 0) {
    const L = list[left]
    if (L % 2 !== 0) remove += 1

    left += 1
  }
  
  answer = Math.max(answer, right - left +1 - (K - remove))
}

console.log(answer)