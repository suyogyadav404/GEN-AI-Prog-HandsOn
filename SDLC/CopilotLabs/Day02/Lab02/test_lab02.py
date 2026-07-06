import pytest
from lab02 import StudentManagement


class TestStudentManagementInit:
    """Test constructor validation and initialization."""

    def test_valid_initialization(self):
        """Test successful student creation with valid inputs."""
        student = StudentManagement(101, "Alice", "Computer Science")
        assert student.student_id == 101
        assert student.student_name == "Alice"
        assert student.department == "Computer Science"
        assert student._is_deleted is False

    def test_invalid_student_id_negative(self):
        """Test that negative student_id raises ValueError."""
        with pytest.raises(ValueError, match="student_id must be a positive integer"):
            StudentManagement(-1, "Alice", "Computer Science")

    def test_invalid_student_id_zero(self):
        """Test that zero student_id raises ValueError."""
        with pytest.raises(ValueError, match="student_id must be a positive integer"):
            StudentManagement(0, "Alice", "Computer Science")

    def test_invalid_student_id_not_int(self):
        """Test that non-integer student_id raises ValueError."""
        with pytest.raises(ValueError, match="student_id must be a positive integer"):
            StudentManagement("101", "Alice", "Computer Science")

    def test_invalid_student_name_empty(self):
        """Test that empty student_name raises ValueError."""
        with pytest.raises(ValueError, match="student_name must be a non-empty string"):
            StudentManagement(101, "", "Computer Science")

    def test_invalid_student_name_whitespace(self):
        """Test that whitespace-only student_name raises ValueError."""
        with pytest.raises(ValueError, match="student_name must be a non-empty string"):
            StudentManagement(101, "   ", "Computer Science")

    def test_invalid_student_name_not_str(self):
        """Test that non-string student_name raises ValueError."""
        with pytest.raises(ValueError, match="student_name must be a non-empty string"):
            StudentManagement(101, 123, "Computer Science")

    def test_invalid_department_empty(self):
        """Test that empty department raises ValueError."""
        with pytest.raises(ValueError, match="department must be a non-empty string"):
            StudentManagement(101, "Alice", "")

    def test_invalid_department_whitespace(self):
        """Test that whitespace-only department raises ValueError."""
        with pytest.raises(ValueError, match="department must be a non-empty string"):
            StudentManagement(101, "Alice", "   ")

    def test_invalid_department_not_str(self):
        """Test that non-string department raises ValueError."""
        with pytest.raises(ValueError, match="department must be a non-empty string"):
            StudentManagement(101, "Alice", 42)


class TestStudentManagementRepr:
    """Test __repr__ method."""

    def test_repr_output(self):
        """Test that __repr__ returns correct format."""
        student = StudentManagement(101, "Alice", "Computer Science")
        expected = "StudentManagement(id=101, name='Alice', dept='Computer Science')"
        assert repr(student) == expected


class TestStudentManagementAddStudent:
    """Test add_student method."""

    def test_add_student_returns_confirmation(self):
        """Test that add_student returns a confirmation message."""
        student = StudentManagement(101, "Alice", "Computer Science")
        result = student.add_student()
        assert "Student added" in result
        assert "101" in result
        assert "Alice" in result
        assert "Computer Science" in result

    def test_add_student_after_deletion_raises_error(self):
        """Test that add_student raises RuntimeError after deletion."""
        student = StudentManagement(101, "Alice", "Computer Science")
        student.delete_student()
        with pytest.raises(RuntimeError, match="Cannot add a deleted student record"):
            student.add_student()


class TestStudentManagementDisplayStudent:
    """Test display_student method."""

    def test_display_student_returns_dict(self):
        """Test that display_student returns a dictionary with correct keys."""
        student = StudentManagement(101, "Alice", "Computer Science")
        result = student.display_student()
        assert isinstance(result, dict)
        assert result["student_id"] == 101
        assert result["student_name"] == "Alice"
        assert result["department"] == "Computer Science"

    def test_display_student_after_deletion_raises_error(self):
        """Test that display_student raises RuntimeError after deletion."""
        student = StudentManagement(101, "Alice", "Computer Science")
        student.delete_student()
        with pytest.raises(RuntimeError, match="Cannot display a deleted student record"):
            student.display_student()


class TestStudentManagementUpdateStudent:
    """Test update_student method."""

    def test_update_student_name_only(self):
        """Test updating only student_name."""
        student = StudentManagement(101, "Alice", "Computer Science")
        result = student.update_student(student_name="Alicia")
        assert student.student_name == "Alicia"
        assert student.department == "Computer Science"
        assert "updated successfully" in result

    def test_update_department_only(self):
        """Test updating only department."""
        student = StudentManagement(101, "Alice", "Computer Science")
        result = student.update_student(department="AI & ML")
        assert student.student_name == "Alice"
        assert student.department == "AI & ML"
        assert "updated successfully" in result

    def test_update_both_fields(self):
        """Test updating both student_name and department."""
        student = StudentManagement(101, "Alice", "Computer Science")
        result = student.update_student(student_name="Alicia", department="Data Science")
        assert student.student_name == "Alicia"
        assert student.department == "Data Science"
        assert "updated successfully" in result

    def test_update_with_no_parameters(self):
        """Test update with no parameters does nothing."""
        student = StudentManagement(101, "Alice", "Computer Science")
        original_name = student.student_name
        original_dept = student.department
        student.update_student()
        assert student.student_name == original_name
        assert student.department == original_dept

    def test_update_student_name_empty_raises_error(self):
        """Test that updating with empty student_name raises ValueError."""
        student = StudentManagement(101, "Alice", "Computer Science")
        with pytest.raises(ValueError, match="student_name must be a non-empty string"):
            student.update_student(student_name="")

    def test_update_student_name_whitespace_raises_error(self):
        """Test that updating with whitespace-only student_name raises ValueError."""
        student = StudentManagement(101, "Alice", "Computer Science")
        with pytest.raises(ValueError, match="student_name must be a non-empty string"):
            student.update_student(student_name="   ")

    def test_update_department_empty_raises_error(self):
        """Test that updating with empty department raises ValueError."""
        student = StudentManagement(101, "Alice", "Computer Science")
        with pytest.raises(ValueError, match="department must be a non-empty string"):
            student.update_student(department="")

    def test_update_department_whitespace_raises_error(self):
        """Test that updating with whitespace-only department raises ValueError."""
        student = StudentManagement(101, "Alice", "Computer Science")
        with pytest.raises(ValueError, match="department must be a non-empty string"):
            student.update_student(department="   ")

    def test_update_after_deletion_raises_error(self):
        """Test that update_student raises RuntimeError after deletion."""
        student = StudentManagement(101, "Alice", "Computer Science")
        student.delete_student()
        with pytest.raises(RuntimeError, match="Cannot update a deleted student record"):
            student.update_student(student_name="Bob")


class TestStudentManagementDeleteStudent:
    """Test delete_student method."""

    def test_delete_student_returns_confirmation(self):
        """Test that delete_student returns a confirmation message."""
        student = StudentManagement(101, "Alice", "Computer Science")
        result = student.delete_student()
        assert "deleted successfully" in result

    def test_delete_student_sets_flag(self):
        """Test that delete_student sets _is_deleted to True."""
        student = StudentManagement(101, "Alice", "Computer Science")
        assert student._is_deleted is False
        student.delete_student()
        assert student._is_deleted is True

    def test_multiple_delete_calls(self):
        """Test that delete_student can be called multiple times."""
        student = StudentManagement(101, "Alice", "Computer Science")
        student.delete_student()
        result = student.delete_student()
        assert "deleted successfully" in result


class TestStudentManagementIntegration:
    """Integration tests for complete workflows."""

    def test_full_lifecycle(self):
        """Test complete workflow: create, display, update, delete."""
        student = StudentManagement(101, "Alice", "Computer Science")
        
        # Add/confirm creation
        add_msg = student.add_student()
        assert "Student added" in add_msg
        
        # Display initial state
        data = student.display_student()
        assert data["student_name"] == "Alice"
        
        # Update
        student.update_student(student_name="Alice Smith", department="AI & ML")
        data = student.display_student()
        assert data["student_name"] == "Alice Smith"
        assert data["department"] == "AI & ML"
        
        # Delete
        delete_msg = student.delete_student()
        assert "deleted successfully" in delete_msg
        
        # Verify deletion prevents operations
        with pytest.raises(RuntimeError):
            student.display_student()

    def test_error_state_isolation(self):
        """Test that errors during update don't corrupt state."""
        student = StudentManagement(101, "Alice", "Computer Science")
        original_dept = student.department
        
        # Try to update with invalid input
        with pytest.raises(ValueError):
            student.update_student(department="")
        
        # State should remain unchanged
        assert student.department == original_dept
