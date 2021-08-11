// --------------- TEMPLATE START ---------------
const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

const nextLine = () => {
  const nextLineGen = (async function* () {
    for await (const line of rl) {
      yield line.trim();
    }
  }());
  return (async () => {
    const next = await nextLineGen.next();
    return next.value;
  })();
};

const nextNum = async () => {
  const line = await nextLine();
  return Number(line);
};

const nextNumArr = async () => {
  const line = await nextLine();
  return line.split(" ").map((num) => Number(num));
};
// --------------- TEMPLATE END ---------------

const ezzatAndTwoSubsequences = async () => {
  let t = await nextNum();
  
  while (t-- > 0) {
    let n = await nextNum();
    let arr = await nextNumArr();
    
    let top = Math.max(...arr);
    let sum = 0;
    for(let i = 0; i < n; i++) {
      sum += arr[i];
    }

    console.log((sum - top) / (n-1) + top);
  }
};

ezzatAndTwoSubsequences();
