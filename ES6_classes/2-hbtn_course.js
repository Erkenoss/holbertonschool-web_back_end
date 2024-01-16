export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = HolbertonCourse.valString(name, 'Name');
    this._length = HolbertonCourse.valNumber(length, 'Length');
    this._students = HolbertonCourse.valArray(students, 'Students');
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    this._name = HolbertonCourse.valString(newName, 'Name');
  }

  get length() {
    return this._length;
  }

  set length(newLength) {
    this._length = HolbertonCourse.valNumber(newLength, 'Length');
  }

  get students() {
    return this._students;
  }

  set students(newStudents) {
    this._students = HolbertonCourse.valArray(newStudents, 'Students');
  }

  static valString(value, propertyName) {
    if (typeof value !== 'string') {
      throw new TypeError(`${propertyName} Must be a string`);
    }
    return value;
  }

  static valNumber(value, propertyName) {
    if (typeof value !== 'number') {
      throw new TypeError(`${propertyName} Must be a number`);
    }
    return value;
  }

  static valArray(value, propertyName) {
    if (!Array.isArray(value)) {
      throw new TypeError(`${propertyName} Must be an array`);
    }
    return value;
  }
}