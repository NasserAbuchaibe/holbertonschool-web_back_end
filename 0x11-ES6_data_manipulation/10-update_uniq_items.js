export default function updateUniqueItems(map) {
  if (map instanceof Map) {
    for (const key of map) {
      if (map.get(key) === 1) {
        map.set(key, 100);
      }
    }
  } else {
    throw Error('Cannot process');
  }
  return map;
}
