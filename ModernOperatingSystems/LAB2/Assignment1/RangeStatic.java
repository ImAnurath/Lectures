package Assignment1;

public class RangeStatic {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Please enter the frequency value as a command line argument.");
            return;
        }
        
        try {
            double frequency = Double.parseDouble(args[0]);
            String range = Frequencies.getFrequencyRange(frequency);
            System.out.println(range);
        } catch (NumberFormatException e) {
            System.out.println("Invalid input. Please enter a valid number for frequency.");
        }
    }
}