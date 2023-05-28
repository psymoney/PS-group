const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = +input.shift()
const matrix = input.map(l => l.split(''))
const matrix2 = input.map(l => l.split(''))
const dir = [[1,0],[0,1],[-1,0],[0,-1]]

let count1 = 0
for (let i in matrix) {
  for (let j in matrix[i]) {
    const char = matrix[i][j]
    if (char !== '') {
      dfs(i * 1, j * 1, matrix, char)
      
      count1 += 1
    }    
  }
}

for (let i in matrix2) {
  for (let j in matrix2[i]) {
    if (matrix2[i][j] === 'R') matrix2[i][j] = 'G'
  }
}


let count2 = 0
for (let i in matrix2) {
  for (let j in matrix2[i]) {
    const char = matrix2[i][j]
    if (char !== '') {
      dfs(i * 1, j * 1, matrix2, char)
      count2 += 1
    }    
  }
}

console.log(count1, count2)


function dfs(i, j, m, char) {
  if (m[i][j] !== char) return

  m[i][j] = ''

  for (let [x, y] of dir) {
    const dx = i + x
    const dy = j + y
    if (dx >= 0 && dx < N && dy >= 0 && dy < N) {
      dfs(dx, dy, m, char)
    }
  }
}