let fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
const N = +input.shift()
const dist = input[0].split(' ').map(BigInt)
const oil = input[1].split(' ').map(BigInt)


let sumCost = oil[0] * dist[0]

let curDist = 1
let prevCost = oil[0]

while (curDist < N-1) {
  const curCost = oil[curDist]
  const nextDist = dist[curDist]

  if (prevCost > curCost) {
    prevCost = curCost
  }

  sumCost += prevCost * nextDist


  curDist += 1
}
console.log(String(sumCost))