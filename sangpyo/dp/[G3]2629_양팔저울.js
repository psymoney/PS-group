const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n"); 
// -------------------------------------------
const N = +input.shift() // <= 30
const WList = input.shift().split(' ').map(Number)
const M = +input.shift() // <= 7
const BList = input.shift().split(' ').map(Number)


const solution = () => {
  let answer = ''
  const dp = Array.from({ length: 31 }, () => new Array(15001).fill(false));

  
  helper(0, 0)

  for (let i = 0; i < M; i++) {
    const x = BList[i]

    if (x > 15000) answer += 'N' + ' '
    else if (dp[N][x]) answer += 'Y' + ' '
    else answer += 'N' + ' '
  }

  console.log(answer.trim())


  function helper(i, w) {
    if (i > N || dp[i][w]) return
    // 가능
    dp[i][w] = true

    // 그대로
    helper(i + 1, w)

    // 구슬
    helper(i + 1, w + WList[i])

    // 구슬 반대
    helper(i + 1, Math.abs(w - WList[i]))
  }
}

solution()