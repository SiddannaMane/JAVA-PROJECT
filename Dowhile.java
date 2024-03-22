import java.util.Scanner;
public class Dowhile
{
    public static void main(String[] args) {
        int n,a,m=0,sum=0;
        Scanner s=new Scanner(System.in);
        System.out.println("enter any number:");
        n=s.nextInt();
        do{
            a=n%10;
            m=m*10+a;
            sum=sum +a;
            n=n/10;
        }
        while(n>0);
        System.out.println("Reverse:"+m);
        System.out.println("sum of digits:"+sum);
        }
    }
