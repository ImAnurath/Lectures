package Ex1;
public class StaticShirt
{
    float price;
    int ID;
    char size;
    public static char convertShirtSize(int numericalSize)
    {
        if (numericalSize < 10)
        {
            return 'S';
        }
        else if (numericalSize < 14)
        {
            return 'M';
        }
        else if (numericalSize < 18)
        {
            return 'L';
        }
        else
        {
            return 'X';
        }
    }
}