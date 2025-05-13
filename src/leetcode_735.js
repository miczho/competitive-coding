/**
 * https://leetcode.com/problems/asteroid-collision/
 * 
 * #2025 #payPal
 */


/**
 * @param {number[]} asteroids
 * @return {number[]}
 */
var asteroidCollision = function (asteroids) {
  let stack = [asteroids[0]]
  let n = asteroids.length

  var getPositiveInt = (num) => {
    return num > 0 ? num : -num
  }
  
  var isColliding = (num1, num2) => {
    return (num1 > 0) && (num2 < 0)
  }

  for (let i = 1; i < n; i++) {
    let x = asteroids[i]

    if (!isColliding(stack[stack.length - 1], x)) {
      stack.push(x)
      continue
    }

    while (stack.length > 0) {
      if (!isColliding(stack[stack.length - 1], x)) {
        stack.push(x)
        break
      } else if (getPositiveInt(stack[stack.length - 1]) > getPositiveInt(x)) {
        break
      } else if (getPositiveInt(stack[stack.length - 1]) < getPositiveInt(x)) {
        stack.pop()

        if (stack.length === 0) {
          stack.push(x)
          break
        }
      } else {
        stack.pop()
        break
      }
    }
  }

  return stack
};
