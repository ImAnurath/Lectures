public class ActivFiltersClass {
    public static void main(String[] args) {
        // Create an object for a low pass filter
        ActivFiltersBasic lpFilter = new ActivFiltersBasic();
        lpFilter.filterType = "Low Pass Filter";
        lpFilter.cutoffFrequency = 1500.0f;
        lpFilter.internalResistance = 100;
        lpFilter.autonomousPowerSupply = true;

        // Create an object for a high pass filter
        ActivFiltersBasic hpFilter = new ActivFiltersBasic();
        hpFilter.filterType = "High Pass Filter";
        hpFilter.cutoffFrequency = 3000.0f;
        hpFilter.internalResistance = 120;
        hpFilter.autonomousPowerSupply = false;

        // Create an object for a band pass filter
        ActivFiltersBasic bpFilter = new ActivFiltersBasic();
        bpFilter.filterType = "Band Pass Filter";
        bpFilter.cutoffFrequency = 2500.0f;
        bpFilter.internalResistance = 110;
        bpFilter.autonomousPowerSupply = true;

        // Display the parameters of the low pass filter
        System.out.println("Low Pass Filter:");
        System.out.println("Filter Type: " + lpFilter.filterType);
        System.out.println("Cut-off Frequency: " + lpFilter.cutoffFrequency + " Hz");
        System.out.println("Internal Resistance: " + lpFilter.internalResistance + " ohms");
        System.out.println("Autonomous Power Supply: " + (lpFilter.autonomousPowerSupply ? "Yes" : "No"));
        System.out.println();

        // Display the parameters of the high pass filter
        System.out.println("High Pass Filter:");
        System.out.println("Filter Type: " + hpFilter.filterType);
        System.out.println("Cut-off Frequency: " + hpFilter.cutoffFrequency + " Hz");
        System.out.println("Internal Resistance: " + hpFilter.internalResistance + " ohms");
        System.out.println("Autonomous Power Supply: " + (hpFilter.autonomousPowerSupply ? "Yes" : "No"));
        System.out.println();

        // Display the parameters of the band pass filter
        System.out.println("Band Pass Filter:");
        System.out.println("Filter Type: " + bpFilter.filterType);
        System.out.println("Cut-off Frequency: " + bpFilter.cutoffFrequency + " Hz");
        System.out.println("Internal Resistance: " + bpFilter.internalResistance + " ohms");
        System.out.println("Autonomous Power Supply: " + (bpFilter.autonomousPowerSupply ? "Yes" : "No"));
    }
}
