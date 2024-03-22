public class datatype 
{
    public static void main(String[]args)
    {
         byte myByte1,myByte2;
         myByte1=120;
         myByte2=-48;
         System.out.println("Byte1:"+myByte1);
         System.out.println("Byte2:"+myByte2);
         myByte1++;//looping back eithin the range
         System.out.println("incremented Value of Byte1:"+myByte1);


         short myShort=6000;
         System.out.println("\nShort:"+myShort);


         int myInteger1, myInteger2, result; 
         myInteger1 = -7000; 
         myInteger2 = 9000;
         result=myInteger1+myInteger2;
         System.out.println("\nInteger1:"+myInteger1); 
         System.out.println("Integer2:"+myInteger2); 
         System.out.println("Integer1 + Integer2: " +result); 
 
         long myLong1, myLong2, result1; 
         myLong1 = 100000000L; 
         myLong2 = 200L; 
         result1 = myLong1 * myLong2; 
         System.out.println("\nLong1: " +myLong1); 
         System.out.println("Long2: " +myLong2); 
         System.out.println("Long1 * Long2: " +result1); 
 
         float myFloat1,myFloat2,result2; 
         myFloat1=1000.666f; 
         myFloat2=110.77f; 
         result2=myFloat1-myFloat2; 
         System.out.println("\nFloat1: "+myFloat1); 
         System.out.println("Float2: "+myFloat2); 
         System.out.println("Float1-Float2: "+result2); 
 
         double myDouble1, myDouble2, result3; 
         myDouble1 = 48976.8987; 
         myDouble2 = 29513.7812d; 
         result3 = myDouble1 + myDouble2; 
         System.out.println("\nDouble1: " +myDouble1); 
         System.out.println("Double2: " +myDouble2); 
         System.out.println("Double1 + Double2: " +result3); 

         boolean myBool = true; 
         if(myBool == true) 
         System.out.println("\nI am using a Boolean data type"); 
         System.out.println(myBool); 
 
         char myChar1 = 'A'; 
         char myChar2 = 66; 
         System.out.println("\nmyChar1: " +myChar1); 
         System.out.println("myChar2: " +myChar2); 
         myChar2++; // valid increment operation
         System.out.println("The Incremented value of myChar2: " +myChar2); 
 
         String string1 = "\nGPT ATHANI"; // declaring string using string literal
         System.out.println(string1);
    }
}



        
 