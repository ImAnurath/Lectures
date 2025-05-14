package Assignment2;

public class Filter3 {
    // Instance variables describing the filter
    int F1;
    int F2;
    String filterType;
    
    // Constructor sets default example values
    public Filter3() {
        F1 = 100;
        F2 = 500;
        filterType = "LPF";
    }
    
    // Overloaded methods to display filter information

    // Option 1: Display filter type only.
    public void print() {
        System.out.println("Filter Type: " + filterType);
    }
    
    // Option 2: Display filter type and starting frequency (F1).
    public void print(int dummy) {
        System.out.println("Filter Type: " + filterType + ", Starting Frequency (F1): " + F1);
    }
    
    // Option 3: Display filter type, starting frequency (F1) and cutoff frequency (F2).
    public void print(int dummy, int dummy2) {
        System.out.println("Filter Type: " + filterType + ", Starting Frequency (F1): " + F1 + ", Cutoff Frequency (F2): " + F2);
    }
    
    // Option 4: Display filter type, starting frequency (F1), cutoff frequency (F2), and bandwidth.
    // Bandwidth is calculated as F2 - F1.
    public void print(int dummy, int dummy2, int dummy3) {
        int bandwidth = F2 - F1;
        System.out.println("Filter Type: " + filterType + ", Starting Frequency (F1): " + F1 +
                           ", Cutoff Frequency (F2): " + F2 + ", Bandwidth: " + bandwidth);
    }
}
