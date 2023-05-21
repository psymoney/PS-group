const fs = require('fs');
2
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
3
let input = fs.readFileSync(filePath).toString().trim().split("\n")
4
​
5
const str = input.shift().split('').map(Number)
6
str.unshift(0)
7
const len = str.length
8
const dp = new Array(len + 1).fill(0)
9
​
10
dp[0] = 1;
11
for (let i = 1; i <= len; i++) {
12
​
13
    if (str[i] != 0) {
14
        dp[i] = (dp[i - 1] + dp[i]) % 1000000;
15
    }
16
​
17
    let x = str[i] + str[i - 1] * 10;
18
​
19
    if (10 <= x && x <= 26) {
20
        dp[i] = (dp[i - 2] + dp[i]) % 1000000;
21
    }
22
}
23
​
24
console.log(dp[len])