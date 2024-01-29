export default function createInt8TypedArray(length, position, value)
{
  if (length < 0 || position >= length) {
    throw new Error('Position outside of range');
  }

  let buffer = new ArrayBuffer(length);
  let int8Array = new Int8Array(buffer);

  int8Array[position] = value;

  return new DataView(buffer);
}
