public class Student
{
    String name; 
    int regno; 
    Student() //Constructor
    {
        name="Raju"; 
        regno=1234;
    }
    Student(String n, int r) // parameterized constructor 
    {
        name=n; 
        regno=r;
    } 
    Student(Student s) // copy constructor 
    {
        name=s.name; 
        regno=s.regno;
    } 
    void display() 
    { 
        System.out.println(name + "\t" +regno); 
    } 
} 
class StudentDemo 
 {
    public static void main(String args[])
    {
        Student s1=new Student(); 
        Student s2=new Student("Ravi",1489); 
        Student s3=new Student(s1);
        s1.display(); 
        s2.display(); 
        s3.display(); 
    } 
 } 

