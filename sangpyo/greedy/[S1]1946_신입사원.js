let fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const [T,...input] = fs.readFileSync(filePath).toString().trim().split('\n');

for(let i=0;i<T;i++) {
  let N = input.shift();
  let Case = input.splice(0,N).map(v=>v.split(' ').map(Number)).sort((a,b) => a[0]-b[0]);
  let answer = 1;
  let top = Case[0][1];
  for(let i=1;i<N;i++) {
    if(Case[i][1]<top) {
      top = Case[i][1];
      answer++;
    }
    if(top===1) break;
  }
  console.log(answer);
}