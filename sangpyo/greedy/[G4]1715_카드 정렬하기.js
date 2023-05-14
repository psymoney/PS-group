class PriorityQueue {
    constructor() {
        this.arr = new Array();
        this.arr.push('');
    }

    push(cost, elem) {
        this.arr.push([cost, elem]);
        let curPosition = this.arr.length-1;

        while (1 < curPosition && this.arr[curPosition][0] < this.arr[Math.floor(curPosition / 2)][0]) {
            let tmp = this.arr[Math.floor(curPosition / 2)];
            this.arr[Math.floor(curPosition / 2)] = this.arr[curPosition];
            this.arr[curPosition] = tmp;
            curPosition = Math.floor(curPosition / 2);
        }
    }

    pop(){
        if(this.arr.length <= 1) return null;
        let curPosition = 1;
        let last = this.arr[curPosition];
        if(2 < this.arr.length) this.arr[curPosition] = this.arr.pop();
        else this.arr.pop();

        while (curPosition * 2 < this.arr.length) {
            if (curPosition * 2 + 1 < this.arr.length && this.arr[curPosition * 2 + 1][0] <= this.arr[curPosition * 2][0] && this.arr[curPosition * 2 + 1][0] < this.arr[curPosition][0]) { //양쪽이 있고 왼쪽이 작을 경우
                    let tmp = this.arr[curPosition * 2 + 1];
                    this.arr[curPosition * 2 + 1] = this.arr[curPosition];
                    this.arr[curPosition] = tmp;
                    curPosition = curPosition * 2 + 1;
            } else if (this.arr[curPosition * 2][0] < this.arr[curPosition][0]){
                let tmp = this.arr[curPosition * 2];
                this.arr[curPosition * 2] = this.arr[curPosition];
                this.arr[curPosition] = tmp;
                curPosition = curPosition * 2;
            } else {
                break;
            }
        }

        return last;
    }
}

const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = +input.shift()
let list = input.map(Number)

// ----------------------------

let sum = 0
const pq = new PriorityQueue()
for (let num of list) {
  pq.push(num, num)
}

while (pq.arr.length > 2) {
  const [w1, v1] = pq.pop()
  const [w2, v2] = pq.pop()
  const s = v1+v2
  sum += s
  pq.push(s, s)
}
console.log(sum)