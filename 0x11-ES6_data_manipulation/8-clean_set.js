export default function cleanSet(set, startString) {
  if (startString && typeof startString === 'string') {
    const valueString = [];
    for (const item of set) {
      if (item.startsWith(startString)) {
        valueString.push(item.slice(startString.length));
      }
    }
    return valueString.join('-');
  }
  return '';
}
