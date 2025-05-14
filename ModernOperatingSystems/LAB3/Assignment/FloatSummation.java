package Assignment;

public class FloatSummation implements Runnable {
    private float upper;
    private FloatSum floatSum;

    public FloatSummation(float upper, FloatSum floatSum) {
        this.upper = upper;
        this.floatSum = floatSum;
    }

    public void run() {
        float sum = 0.0f;
        for (float i = 0.0f; i <= upper; i += 0.5f) {
            sum += i;
        }
        floatSum.setSum(sum);
    }
}