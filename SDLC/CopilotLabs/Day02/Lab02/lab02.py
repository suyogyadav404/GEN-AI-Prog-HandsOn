class StudentManagement:
    def __init__(self, student_id: int, student_name: str, department: str) -> None:
        """Initialize a student record with validation."""
        if not isinstance(student_id, int) or student_id <= 0:
            raise ValueError("student_id must be a positive integer")
        if not isinstance(student_name, str) or not student_name.strip():
            raise ValueError("student_name must be a non-empty string")
        if not isinstance(department, str) or not department.strip():
            raise ValueError("department must be a non-empty string")
        
        self.student_id: int = student_id
        self.student_name: str = student_name
        self.department: str = department
        self._is_deleted: bool = False

    def __repr__(self) -> str:
        """Return a developer-friendly string representation."""
        return (
            f"StudentManagement(id={self.student_id}, "
            f"name={self.student_name!r}, dept={self.department!r})"
        )

    def add_student(self) -> str:
        """Returns a confirmation message for adding a student."""
        if self._is_deleted:
            raise RuntimeError("Cannot add a deleted student record")
        return (
            f"Student added: ID={self.student_id}, "
            f"Name={self.student_name}, Department={self.department}"
        )

    def display_student(self) -> dict:
        """Returns student details as a dictionary."""
        if self._is_deleted:
            raise RuntimeError("Cannot display a deleted student record")
        return {
            "student_id": self.student_id,
            "student_name": self.student_name,
            "department": self.department,
        }

    def update_student(self, student_name: str | None = None, department: str | None = None) -> str:
        """Updates student name and/or department with validation."""
        if self._is_deleted:
            raise RuntimeError("Cannot update a deleted student record")
        
        if student_name is not None:
            if not isinstance(student_name, str) or not student_name.strip():
                raise ValueError("student_name must be a non-empty string")
            self.student_name = student_name
        
        if department is not None:
            if not isinstance(department, str) or not department.strip():
                raise ValueError("department must be a non-empty string")
            self.department = department
        
        return "Student record updated successfully."

    def delete_student(self) -> str:
        """Marks student record as deleted."""
        self._is_deleted = True
        return "Student record deleted successfully."
    
    def search_student_by_id(self, student_id: int) -> dict | None:
        """Searches for a student by ID and returns their details if found."""
        if self._is_deleted:
            raise RuntimeError("Cannot search a deleted student record")
        if self.student_id == student_id:
            return self.display_student()
        return None


if __name__ == "__main__":
    student = StudentManagement(101, "Aarav", "Computer Science")
    print(student.add_student())
    print(student.display_student())

    print(student.update_student(student_name="Aarav Sharma", department="AI & DS"))
    print(student.display_student())

    print(student.delete_student())
    # Removed the invalid call to display_student() after deletion
    # Instead, demonstrate error handling:
    try:
        print(student.display_student())
    except RuntimeError as e:
        print(f"Error: {e}")

    # Demonstrate searching for a student by ID
    try:
        student_details = student.search_student_by_id(101)
        if student_details:
            print(f"Student found: {student_details}")
        else:
            print("Student not found.")
    except RuntimeError as e:
        print(f"Error: {e}")
