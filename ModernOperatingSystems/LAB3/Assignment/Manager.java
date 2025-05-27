package Assignment;

public class Manager {
    public static void main(String[] args) {
        if (args.length > 1) {
            try {
                int upperInt = Integer.parseInt(args[0]);
                float upperFloat = Float.parseFloat(args[1]);

                if (upperInt < 0 || upperFloat < 0) {
                    System.err.println("Both values must be >= 0.");
                    return;
                }

                // Objects to hold results
                Sum intSum = new Sum();
                FloatSum floatSum = new FloatSum();

                // Create and start threads
                Thread worker1 = new Thread(new Summation(upperInt, intSum));
                Thread worker2 = new Thread(new FloatSummation(upperFloat, floatSum));

                worker1.start();
                worker2.start();

                worker1.join();
                worker2.join();

                System.out.println("Sum of integers from 0 to " + upperInt + " is: " + intSum.getSum());
                System.out.println("Sum of real numbers from 0 to " + upperFloat + " (in steps of 0.5) is: " + floatSum.getSum());

            } catch (NumberFormatException e) {
                System.err.println("Invalid input. Provide an integer and a float.");
            } catch (InterruptedException e) {
                System.err.println("Thread interrupted.");
            }
        } else {
            System.err.println("Usage: Manager <integer value> <float value>");
        }
    }
}
