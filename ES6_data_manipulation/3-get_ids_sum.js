export default function getStudentIdsSum(getListStudents)
{
  return getListStudents.reduce((acc, array) => acc + array, 0);
}
