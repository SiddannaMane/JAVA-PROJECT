 class Encapsulate {
    //private variables declared these can only be accessed by methods of class
    private String geekName;
    private int geekRoll;
    private int geekAge;

    public void setAge(int newAge) // set method for name to access private variable geekage
    {
        geekAge=newAge;
    }
    public void setName(String  newName) // set method for name to access private variable geekName
    {
        geekName=newName;
    }
    public void setRoll(int newRoll) // set method for name to access private variable geekRoll
    {
        geekRoll=newRoll;
    }
    public String getName() // set method for name to access private variable geekName
    {
        return geekName;
    }
    public int getRoll()
    {
        return geekRoll;
    }
    public int getAge()
    {
        return geekAge;
    }
}

public class EncapsulationDemo
{
    public static void main(String[]args)
    {
        Encapsulate obj=new Encapsulate();//creating object
        //setting values of the variables using set methods

        obj.setName("harish");
        obj.setAge(19);
        obj.setRoll(51);

        System.out.println("geek's name:"+obj.getName());
        System.out.println("geek's age:"+obj.getAge());
        System.out.println("geek's roll:"+obj.getRoll());
    }
}

