let obj = {
  x: 10,
  y: 20,
  show: function () {
    console.log(this.x, this.y)
  }
}

let arr = [1, 2]

obj.show()
console.log(Object.getOwnPropertyNames(obj))
console.log(Object.getOwnPropertyNames(Array.prototype))

// var myButton = {
//   content: 'OK',
//   click() {
//     console.log(this.content + ' clicked');
//   }
// };

// myButton.click();

// var looseClick = myButton.click;
// looseClick(); // not bound, 'this' is not myButton - it is the globalThis

// var boundClick = myButton.click.bind(myButton);
// boundClick(); // bound, 'this' is myButton