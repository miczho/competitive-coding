// --------------- PRE-DEFINED START ---------------
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

const nextBigIntArr = async () => {
  const line = await nextLine();
  return line.split(" ").map((num) => BigInt(num));
};

const sortAsc = (a, b) => {
   if (a < b) return -1;
   if (a > b) return 1;
   return 0;
}
// --------------- PRE-DEFINED END ---------------

const main = async () => {
  let [n, k, x] = await nextBigIntArr();
  let arr = await nextBigIntArr();

  let gaps = [];

  arr.sort(sortAsc);
  for (let i = 1; i < n; i++) {
    const tmp = arr[i] - arr[i-1];
    if (tmp > x) gaps.push((tmp / x) - (tmp % x === 0n ? 1n : 0n));
  }

  gaps.sort(sortAsc);
  let res = gaps.length + 1;
  for (let i = 0; i < gaps.length; i++) {
    if (gaps[i] > k) break;
    k -= gaps[i];
    res -= 1;
  }

  console.log(res);
};

main();
