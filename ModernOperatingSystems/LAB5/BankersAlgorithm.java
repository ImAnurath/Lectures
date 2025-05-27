public class BankersAlgorithm {

    static int n = 5; // number of processes
    static int m = 3; // number of resource types

    // Safe
    // static int[][] allocation = {
    //     {0, 1, 0}, // # of A B C
    //     {2, 0, 0},
    //     {3, 0, 2},
    //     {2, 1, 1},
    //     {0, 0, 2}
    // };
    // static int[][] max = {
    //     {7, 5, 3}, // # of need for A B C
    //     {3, 2, 2},
    //     {9, 0, 2},
    //     {2, 2, 2},
    //     {4, 3, 3}
    // };
    // static int[] available = {3, 3, 2}; // # of free A B C


    
    // Unsafe
    static int[][] allocation = {
    {1, 0, 2},
    {1, 2, 1},
    {1, 3, 1},
    {1, 0, 0},
    {0, 2, 2}
    };

    static int[][] max = {
    {3, 2, 2},
    {1, 2, 2},
    {1, 3, 5},
    {1, 1, 0},
    {3, 3, 3}
    };
    static int[] available = {0, 0, 0};


    static int[][] need = new int[n][m];
    /*  Need => is the difference between the maximum and the allocated resources.
     *  If the sum of the need of a process is greater than the available resources, it is not safe.
     */
    public static void calculateNeed() { 
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                need[i][j] = max[i][j] - allocation[i][j];
    }

    public static boolean isSafe() {
        boolean[] finish = new boolean[n];
        int[] work = available.clone();
        int[] safeSeq = new int[n];
        int count = 0;
        while (count < n) { // Runs until all processes have been assigned
            boolean found = false;
            for (int i = 0; i < n; i++) { // Checks if process i is finished
                if (!finish[i]) { // If process i is not finished 
                    int j;
                    for (j = 0; j < m; j++)
                        if (need[i][j] > work[j]) // If pocess i needs more than available resources then it is not safe, so break it
                            break;

                    if (j == m) { // if it is not finished and does not need more than available resources
                        for (int k = 0; k < m; k++)
                            work[k] += allocation[i][k];
                        safeSeq[count++] = i; // Add process i to safe sequence
                        finish[i] = true;
                        found = true; // Meaning a safe sequence has been found, so the system is safe to run
                    }
                }
            }

            if (!found) {
                System.out.println("System is NOT in a safe state."); // Happens when we break on line 64
                return false;
            } 
        }

        System.out.print("System is in a safe state.\nSafe sequence: ");
        for (int i = 0; i < n; i++)
            System.out.print("T" + safeSeq[i] + " ");
        System.out.println();
        return true;
    }

    public static void main(String[] args) {
        calculateNeed();
        isSafe();
    }
}
