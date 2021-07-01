export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const view = new Int8Array(buffer);
  const lengthArray = length;
  if (position >= lengthArray) {
    throw Error('Position outside range');
  }
  view[position] = value;
  const dataView = new DataView(buffer);
  return dataView;
}
