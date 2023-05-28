const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [row, col] = input.shift().split(' ').map(Number)
const list = input.map(l => l.split(' ').map(Number))

const dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
const isVal = (x, y) => x >= 0 && x < row && y >= 0 && y < col

let years = 0
while (true) {
  melt()
  years += 1

  const count = find()
  if (count === 0) return console.log(0)
  if (count >= 2) return console.log(years)
}
// 빙하 녹이기
function melt() {
  // 빙하 찾기
  const iceList = []
  for (let i in list) {
    for (let j in list[i]) {
      if (list[i][j] > 0) {
        let zeroCount = 0
        for (let [x, y] of dir) {
          const dx = i*1 + x
          const dy = j*1 + y
          if (isVal(dx, dy) && list[dx][dy] === 0) {
            zeroCount += 1
          }
        }
        iceList.push([i*1, j*1, zeroCount])
      }
    }
  }
  // 빙하녹이기
  for (let [x, y, z] of iceList) {
    list[x][y] = Math.max(0, list[x][y] - z)
  }
}

// 몇조각인지 찾기.
function find() {
  const visited = Array.from({ length: row }, () => new Array(col).fill(false))
  let count = 0
  for (let i in list) {
    for (let j in list[i]) {
      if (!visited[i][j] && list[i][j] > 0) {
        count += 1
        bfs(i*1, j*1, visited)
      }
    }
  }
  return count
}

function bfs(i, j, visited) {
  let q = [[i, j]]
  while (q.length) {
    const temp = []

    for (let [i, j] of q) {
      if (visited[i][j]) continue
      visited[i][j] = true

      for (let [x, y] of dir) {
        const dx = i + x
        const dy = j + y
        if (isVal(dx, dy) && list[dx][dy] > 0) {
          temp.push([dx, dy])
        }
      }

    }
    q = temp
  }
}