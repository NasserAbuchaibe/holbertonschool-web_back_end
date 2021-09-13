export default function appendToEachArrayValue(array, appendString) {
    const arrayA = array;
    for (const value of array) {
        const idx = array.indexOf(value);
        arrayA[idx] = appendString + value;
    }

    return arrayA;
}
