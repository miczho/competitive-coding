const fido = {
  name: "Fido",
  breed: "Schnauzer",
  bark(message) {
    console.log(`${this.name} the ${this.breed} says, '${message}'`)
  },
}

const f = Object.create(fido)
f.bark('my asscrack')