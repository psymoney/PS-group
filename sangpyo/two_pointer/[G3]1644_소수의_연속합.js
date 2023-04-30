const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
const N = +input.shift()

if (N === 1) return console.log(0)

// 에라토스테네스의 채
function eratosthenesSieve(number) {
    const array = [];
    const tempArray = [];

    for (let i = 2; i <= number; i++) tempArray[i] = i;

    for (let i = 2; i <= number; i++) {
        if (tempArray[i] === 0) continue;
        for (let j = i + i; j <= number; j += i) tempArray[j] = 0;
    }

    for (let i = 2; i <= number; i++) {
        if (tempArray[i] !== 0) array.push(tempArray[i]);
    }

    return array;
}

const prime = eratosthenesSieve(N)

let left = 0, right = 0, sum = 0, cnt = 0

for (right; right < prime.length; right++) {
  sum += prime[right];
  while (sum > N) {
    sum -= prime[left];
    left++;
  }
  if (sum === N) cnt++;
}
console.log(cnt);