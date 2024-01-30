export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  const studentsInCity = getListStudents.filter((student) => student.location.includes(city));

  const updatedStudents = studentsInCity.map((student) => {
    const matchingGrade = newGrades.find((grade) => grade.studentId === student.id);

    if (matchingGrade) {
      return { ...student, grade: matchingGrade.grade };
    }
    return { ...student, grade: 'N/A' };
  });

  return updatedStudents;
}
