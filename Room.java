class Room
{
    int length,breadth;
    Room(int x,int y)
    {
        length =x;
        breadth =y;
    }
    int area()
    {
        return(length*breadth);
    }
}
class ClassRoom extends Room
{
    int heigth;
    ClassRoom(int x,int y,int z)
    {
        super(x,y);
        heigth =z;
    }
    int volume()
    {
        return(length*breadth*heigth);
    }
}
class SubClass
{
    public static void main(String args[])
    {
        ClassRoom cr=new ClassRoom(20,30,10);
        int area =cr.area();
        int volume=cr.volume();

        System.out.println("Area="+area);
        System.out.println("Volume="+volume);
    }
}