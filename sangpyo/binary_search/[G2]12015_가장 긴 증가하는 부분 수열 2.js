const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = +input.shift();
const arr = input[0].split(' ').map(Number);


function binarySearch(left, right, target) {

  while (left < right) {
    const mid = (left + right) >>> 1

    if (lis[mid] < target) {
      left = mid + 1;
    } else {
      right = mid
    }
  }
  return right;
}

let lis = [];

let j = 0;
lis[0] = arr[0];
let i = 1;

while (i < N) {
  if (lis[j] < arr[i]) {
    lis[++j] = arr[i];
  } else {
    let idx = binarySearch(0, j, arr[i]);
    lis[idx] = arr[i]
  }
  i++;
}
console.log(lis.length)