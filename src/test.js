// What does this refer to when you invoke a function as a method (that is, 
// you call a function from an object)? For example:
//

function foo() {
    console.log(this);
}
const obj = {x: 123, foo: foo};
obj.foo();