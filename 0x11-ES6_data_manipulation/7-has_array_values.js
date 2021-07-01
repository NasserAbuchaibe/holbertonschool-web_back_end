export default function hasValuesFromArray(set, array) {
  const elemt = array.every((item) => set.has(item));
  return elemt;
}
