const a = new ArrayBuffer(8)
console.log(a)

const a32 = new Uint32Array(a)
console.log(a32)

const a8 = new Uint8Array(a)
console.log(a8)

a32[0] = 4294967295
console.log(a32)
console.log(a8)
console.log(a)