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
  
};

main();
