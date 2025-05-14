package Assignment2;

public class CreateFilter3 {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Please enter an option number (1 to 4) as a command line argument.");
            return;
        }
        
        int option = Integer.parseInt(args[0]);
        Filter3 filter = new Filter3();
        
        switch (option) {
            case 1:
                filter.print();
                break;
            case 2:
                filter.print(0); // dummy argument to select the second overload
                break;
            case 3:
                filter.print(0, 0); // dummy arguments for the third overload
                break;
            case 4:
                filter.print(0, 0, 0); // dummy arguments for the fourth overload
                break;
            default:
                System.out.println("Invalid option. Please enter a number between 1 and 4.");
        }
    }
}
