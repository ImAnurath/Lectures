/**
 * Petersons.java
 *
 * This program implements strict alternation as a means of handling synchronization.
 *
 * Note - Using an array for the two flag variables would be preferable, however, we must
 * declare the data as volatile, and volatile does not extend to arrays.
 */

 public class Petersons implements MutualExclusion {
    private volatile int turn;
    private volatile boolean flag0;
    private volatile boolean flag1;

    public Petersons() {
        flag0 = false;
        flag1 = false;
        turn = 0;
    }

    public void entrySection(int t) {
        int other = 1 - t; // Get the index of the other thread

        if (t == 0) {
            flag0 = true; // Indicate interest in entering the critical section
            turn = other; // Give priority to the other thread
            
            // Wait while the other thread is interested and it is their turn
            while (flag1 && turn == other) {
                System.out.println("Thread 0 waiting: flag1=" + flag1 + ", turn=" + turn);
                Thread.yield();
            }
        } else {
            flag1 = true; // Indicate interest in entering the critical section
            turn = other; // Give priority to the other thread
            
            // Wait while the other thread is interested and it is their turn
            while (flag0 && turn == other) {
                System.out.println("Thread 1 waiting: flag0=" + flag0 + ", turn=" + turn);
                Thread.yield();
            }
        }
    }

    public void exitSection(int t) {
        if (t == 0) {
            flag0 = false; // Indicate that thread 0 is leaving the critical section
            System.out.println("Thread 0 exiting: flag0=" + flag0);
        } else {
            flag1 = false; // Indicate that thread 1 is leaving the critical section
            System.out.println("Thread 1 exiting: flag1=" + flag1);
        }
    }
}
