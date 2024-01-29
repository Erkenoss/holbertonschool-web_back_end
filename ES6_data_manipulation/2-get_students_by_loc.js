export default function getStudentsByLocation(getListStudents, city)
{
  const studentCity = getListStudents.filter(student => student.location.includes(city));

  return studentCity;
}