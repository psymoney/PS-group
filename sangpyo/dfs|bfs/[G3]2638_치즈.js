const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [row, col] = input.shift().split(' ').map(Number)
const list = input.map(l => l.split(' ').map(Number))

const dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
const isVal = (x, y) => x >= 0 && x < row && y >= 0 && y < col

let times = 0

while (true) {
  const res = bfs()
  if (!res) break;
  times += 1
}

console.log(times)

// 치즈의 표면 찾기
function bfs() {
  const surface = []
  let q = [[0, 0]]
  const visited = Array.from({ length: row }, () => new Array(col).fill(false))
  
  while (q.length) {
    const temp = []
    
    for (let [i, j] of q) {
      if (visited[i][j]) continue
      visited[i][j] = true
      
      for (let [x, y] of dir) {
        const dx = i + x
        const dy = j + y
        if (isVal(dx, dy)) {
          if (list[dx][dy] === 1 && !visited[dx][dy]) {
            surface.push([dx, dy])
            visited[dx][dy] = true
          }
          else temp.push([dx, dy])
        }
      }
    }
    q = temp
  }
  // 녹이기
  let check = false
  if (surface.length > 0) check = true
  findTwoSurface(surface, visited)
  return check
}

function findTwoSurface(arr, visited) {
  let t = []
  for (let [i, j] of arr) {
    let count = 0
    for (let [x, y] of dir) {
      const dx = i + x
      const dy = j + y
      if (isVal(dx, dy) && list[dx][dy] === 0 && visited[dx][dy]) {
        count += 1
      }
    }

    if (count >= 2) {
      t.push([i, j])
    }
  }


  for (let [i, j] of t) {
    list[i][j] = 0
  }
}