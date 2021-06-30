export default function getListStudentIds (students) {
    // if it is an array we map the ids
    if (Array.isArray(students)) {
      return students.map((items) => items.id);
    }
    return [];
  }
