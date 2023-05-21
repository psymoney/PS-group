let fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
const s1 = input.shift()
const s2 = input.shift()


function LCS(text1, text2) {
    const col = text1.length
    const row = text2.length
    const memo = Array.from({length: col+1}, () => new Array(row+1))

  
    function recursion(i, j) {
        if (i === text1.length || j === text2.length) return 0;
        if (memo[i][j] !== undefined) return memo[i][j]
        if (text1.charAt(i) === text2.charAt(j)) {
            memo[i][j] = 1 + recursion(i + 1, j + 1)
            return memo[i][j];
        }

        memo[i][j] = Math.max(recursion(i + 1, j), recursion(i, j + 1));
        return memo[i][j]
    }

    return recursion(0, 0)
};

const res = LCS(s1, s2)

console.log(res)