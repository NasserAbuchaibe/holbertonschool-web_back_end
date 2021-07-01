export default function getStudentIdsSum(myOb) {
  if (Array.isArray(myOb) === false) {
    return [];
  }
  const reducer = (accumulator, currentValue) => accumulator + currentValue.id;
  return myOb.reduce(reducer, 0);
}
