export default function getListStudentIds(getListStudents)
{
  if (!Array.isArray(getListStudents)) {
    return [];
  }
  const studentsIds = getListStudents.map(student => student.id);

  return studentsIds;
}
