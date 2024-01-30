export default function getStudentsByLocation(getListStudents, city) {
  const studentCity = getListStudents.filter((student) => student.location === (city));

  return studentCity;
}
