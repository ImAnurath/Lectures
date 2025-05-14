public class Reactance {
    public static void main(String[] args) {
        double capacitance = Double.parseDouble(args[0]);
        double inductance  = Double.parseDouble(args[1]);
        double frequency   = Double.parseDouble(args[2]);
        
        double angularFrequency = 2 * Math.PI * frequency;
        
        double inductiveReactance = angularFrequency * inductance;
        
        double capacitiveReactance = 1.0 / (angularFrequency * capacitance);
        
        // Display the results.
        System.out.println("Inductive Reactance: " + inductiveReactance + " ohms");
        System.out.println("Capacitive Reactance: " + capacitiveReactance + " ohms");
    }
}
