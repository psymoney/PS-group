const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
const [N, K] = input.shift().split(' ').map(Number)
const list = input.map(l => l.split(' ').map(Number))

const dp = Array.from({ length: N + 1 }, () => new Array(K + 1))
for (let i = 0; i <= N; i++) {
  dp[i][0] = 0
}
for (let i = 0; i <= K; i++) {
  dp[0][i] = 0
}

for (let n = 1; n <= N; n++) {
  const [weight, value] = list[n-1];
  for (let k = 0; k <= K; k++) {
    //물건의 무게가 k보다 클 때
    if (k < weight) {
      dp[n][k] = dp[n - 1][k];
    } else {
      dp[n][k] = Math.max(
        dp[n - 1][k], //n번 물건 안 담는 경우
        dp[n - 1][k - weight] + value //n번 물건 담는 경우
      );
    }
  }
}

console.log(dp[N][K])