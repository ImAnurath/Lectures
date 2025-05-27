package Ex2;
//overloaded methods


public class Shirt3
{
    int itemID;
    String shirtType;
    float price ;
	
    //overloaded methods
	
    public void print(float thePrice)
    {
        System.out.println(thePrice);
    }
	
    public void print(float thePrice, int theID)
    {
        System.out.println(thePrice + " " + theID);
    }
	
    public void print(float thePrice, int theID, String theType)
    {
        System.out.println(thePrice + " " + theID + " " + theType);
    }
	
    // end overloaded methods 
	
	
    public int getItemID()
    {
	
        return itemID;
		
    }// end getItemID()
	
    public float getPrice()
    {
	
        return price;
	
    }//end getPrice()
	
    public String getShirtType()
    {
	
        return shirtType;	
	
    }//end getShirtType()
	
	
    public void setItemID(int newItemID)
    {
	
        itemID = newItemID;
	
    }// end setItemID()
	
    public void setShirtType(String newShirtType)
    {
	
        shirtType = newShirtType;
	
    }//end setShirtType()
	
    public void setPrice(float newPrice)
    {
	
        price = newPrice;

    }//end setPrice()

}//end class