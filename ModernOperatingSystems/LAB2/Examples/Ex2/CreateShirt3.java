package Ex2;
//calling overloaded methods

public class CreateShirt3
{
    public static void main(String args[])
    {
	
        Shirt3 newShirt = new Shirt3();
		
        newShirt.print(3.4F);
        newShirt.print(3.4F, 3);
        newShirt.print(3.4F, 3, "Western Yoke");
		
    }// end main

}//end class