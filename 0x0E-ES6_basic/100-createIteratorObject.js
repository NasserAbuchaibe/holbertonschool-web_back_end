export default function createIteratorObject(report) {
    let listResult = [];
    for (const value of Object.values(report.allEmployees)) {
        listResult = [...listResult, ...value];
    }

    return listResult;
}
