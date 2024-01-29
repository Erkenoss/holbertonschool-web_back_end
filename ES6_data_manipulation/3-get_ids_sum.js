export default function getStudentIdsSum(getListStudents)
{
  return getListStudents.reduce((acc, array) => acc + array.id, 0);
}
