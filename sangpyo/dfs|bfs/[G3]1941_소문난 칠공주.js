const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
const M = input.map(l => l.split(''))
const dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
let answer = 0

function Comb(arr, index, count, left) { // 조합찾기
  if (left === 0) {
    BFS(arr) // 노드들 연결확인, S 4개이상 확인
    return 
  }

  if(count == 25) return;

  arr[index] = count
  Comb(arr,index+1, count+1, left-1);
  Comb(arr,index,count+1,left);

}

function BFS(comb) {
  let q = []
  const visited = new Array(7).fill(false)
  q.push(comb[0])

  let count = 0, countS = 0;
  while (q.length) {
    const temp = []
    for (let cur of q) {
      if (visited[cur]) continue
      visited[cur] = true
      count++
      const i = Math.floor(cur / 5)
      const j = Math.floor(cur % 5)
      if (M[i][j] === 'S') countS += 1

      for (let [x, y] of dir) {
        const dx = i + x
        const dy = j + y
        for (let j = 1; j < 7; j++) {
          const next = comb[j]
          const nextI = Math.floor(next / 5)
          const nextJ = Math.floor(next % 5)
          if (dx === nextI && dy === nextJ) {
            temp.push(comb[j])
            
          }
        }
      }

    }
    q = temp
  }
  if(count == 7 && countS >= 4) answer += 1
}

Comb([], 0, 0, 7)
console.log(answer)