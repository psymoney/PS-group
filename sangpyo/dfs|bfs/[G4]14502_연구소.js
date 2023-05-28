const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [col, row] = input.shift().split(' ').map(Number);
const board = input.map((i) => i.split(' ').map(Number));

const dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
const isVal = (x, y) => x >= 0 && x < row && y >= 0 && y < col

let answer = 0;

const bfs = (arr) => {
  let cnt = 0;
  let q = [];

  // 1. 바이러스들 큐에 넣기
  for (let i = 0; i < col; i++) {
    for (let j = 0; j < row; j++) {
      if (arr[i][j] === 2) q.push([i, j]);
    }
  }

  // 2. 바이러스들 전염
  while (q.length) {
    const temp = []

    for (let [curX, curY] of q) {
      
      for (let [x, y] of dir) {
        const dx = curX + x, dy = curY + y
 
        if (isVal(dx, dy) && arr[dx][dy] === 0) {
          arr[dx][dy] = 2;
          q.push([dx, dy]);
        }
      }
    }
    
    q = temp
  }

  // 3. 안전영역 세기
  for (let i = 0; i < col; i++) {
    for (let j = 0; j < row; j++) {
      if (arr[i][j] === 0) {
        cnt += 1;
      }
    }
  }

  return cnt;
};

// 벽의 조합찾기
const combination = (cnt) => {
  if (cnt === 3) {
    let arr = board.map((v) => [...v]);
    
    let res = bfs(arr);

    answer = Math.max(answer, res);
    return;
  }

  for (let i = 0; i < col; i++) {
    for (let j = 0; j < row; j++) {
      if (board[i][j] === 0) {
        board[i][j] = 1;
        combination(cnt + 1);
        board[i][j] = 0;
      }
    }
  }
};

combination(0);

console.log(answer);