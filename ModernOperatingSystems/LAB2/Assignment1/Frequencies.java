package Assignment1;

public class Frequencies {
    public static String getFrequencyRange(double frequency) {
        // Frequency ranges are assumed to be in Hertz (Hz)
        if (frequency >= 300 && frequency < 30000) {
            return "Very low frequencies (3 30 kHz)";
        } else if (frequency >= 30000 && frequency < 300000) {
            return "Low frequencies (30 300 kHz)";
        } else if (frequency >= 300000 && frequency < 3000000) {
            return "Middle frequencies (0.3 3 MHz)";
        } else if (frequency >= 3000000 && frequency < 30000000) {
            return "High frequencies (3 30 MHz)";
        } else if (frequency >= 30000000 && frequency < 300000000) {
            return "Very high frequencies (30 300 MHz)";
        } else if (frequency >= 300000000 && frequency < 3000000000.0) {
            return "Ultra-high frequencies (0.3 3 GHz)";
        } else if (frequency >= 3000000000.0 && frequency < 30000000000.0) {
            return "Super high frequencies (3 30 GHz)";
        } else if (frequency >= 30000000000.0 && frequency < 300000000000.0) {
            return "Extra high frequencies (30 300 GHz)";
        } else if (frequency >= 300000000000.0 && frequency < 3000000000000.0) {
            return "Hyper high frequencies (300 3000 GHz)";
        } else {
            return "Frequency out of defined range";
        }
    }
}
