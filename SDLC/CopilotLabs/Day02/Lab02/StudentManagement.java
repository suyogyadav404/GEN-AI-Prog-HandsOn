import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

/**
 * StudentManagement class represents a student record with validation.
 * Provides CRUD operations on a single student entity.
 */
public class StudentManagement {
    private int studentId;
    private String studentName;
    private String department;
    private boolean isDeleted;

    /**
     * Constructor to initialize a student record with validation.
     *
     * @param studentId   must be a positive integer
     * @param studentName must be a non-empty string
     * @param department  must be a non-empty string›
     * @throws IllegalArgumentException if any parameter is invalid
     */
    public StudentManagement(int studentId, String studentName, String department) {
        if (studentId <= 0) {
            throw new IllegalArgumentException("student_id must be a positive integer");
        }
        if (studentName == null || studentName.trim().isEmpty()) {
            throw new IllegalArgumentException("student_name must be a non-empty string");
        }
        if (department == null || department.trim().isEmpty()) {
            throw new IllegalArgumentException("department must be a non-empty string");
        }

        this.studentId = studentId;
        this.studentName = studentName;
        this.department = department;
        this.isDeleted = false;
    }

    /**
     * Returns a developer-friendly string representation of the student.
     *
     * @return formatted string representation
     */
    @Override
    public String toString() {
        return String.format(
            "StudentManagement(id=%d, name='%s', dept='%s')",
            studentId, studentName, department
        );
    }

    /**
     * Returns a confirmation message for adding a student.
     *
     * @return confirmation message
     * @throws RuntimeException if student record is deleted
     */
    public String addStudent() {
        if (isDeleted) {
            throw new RuntimeException("Cannot add a deleted student record");
        }
        return String.format(
            "Student added: ID=%d, Name=%s, Department=%s",
            studentId, studentName, department
        );
    }

    /**
     * Returns student details as a HashMap.
     *
     * @return map containing student_id, student_name, and department
     * @throws RuntimeException if student record is deleted
     */
    public Map<String, Object> displayStudent() {
        if (isDeleted) {
            throw new RuntimeException("Cannot display a deleted student record");
        }
        Map<String, Object> studentData = new HashMap<>();
        studentData.put("student_id", studentId);
        studentData.put("student_name", studentName);
        studentData.put("department", department);
        return studentData;
    }

    /**
     * Updates student name and/or department with validation.
     *
     * @param studentName optional new student name (null to skip update)
     * @param department  optional new department (null to skip update)
     * @return success message
     * @throws RuntimeException        if student record is deleted
     * @throws IllegalArgumentException if provided values are invalid
     */
    public String updateStudent(String studentName, String department) {
        if (isDeleted) {
            throw new RuntimeException("Cannot update a deleted student record");
        }

        if (studentName != null) {
            if (studentName.trim().isEmpty()) {
                throw new IllegalArgumentException("student_name must be a non-empty string");
            }
            this.studentName = studentName;
        }

        if (department != null) {
            if (department.trim().isEmpty()) {
                throw new IllegalArgumentException("department must be a non-empty string");
            }
            this.department = department;
        }

        return "Student record updated successfully.";
    }

    /**
     * Marks student record as deleted.
     *
     * @return deletion confirmation message
     */
    public String deleteStudent() {
        this.isDeleted = true;
        return "Student record deleted successfully.";
    }

    /**
     * Searches for a student by ID and returns their details if found.
     *
     * @param studentId ID to search for
     * @return student details if found, null otherwise
     * @throws RuntimeException if student record is deleted
     */
    public Map<String, Object> searchStudentById(int studentId) {
        if (isDeleted) {
            throw new RuntimeException("Cannot search a deleted student record");
        }
        if (this.studentId == studentId) {
            return displayStudent();
        }
        return null;
    }

    /**
     * Main method to demonstrate StudentManagement functionality.
     *
     * @param args command-line arguments (not used)
     */
    public static void main(String[] args) {
        // Create a new student
        StudentManagement student = new StudentManagement(101, "Aarav", "Computer Science");
        System.out.println(student.addStudent());
        System.out.println(student.displayStudent());

        // Update student record
        System.out.println(student.updateStudent("Aarav Sharma", "AI & DS"));
        System.out.println(student.displayStudent());

        // Delete student
        System.out.println(student.deleteStudent());

        // Demonstrate error handling when accessing deleted record
        try {
            System.out.println(student.displayStudent());
        } catch (RuntimeException e) {
            System.out.println("Error: " + e.getMessage());
        }

        // Demonstrate searching for a student by ID
        try {
            Map<String, Object> studentDetails = student.searchStudentById(101);
            if (studentDetails != null) {
                System.out.println("Student found: " + studentDetails);
            } else {
                System.out.println("Student not found.");
            }
        } catch (RuntimeException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
