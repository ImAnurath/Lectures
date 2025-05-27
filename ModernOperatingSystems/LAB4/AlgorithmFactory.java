/**
 * AlgorithmFactory.java
 *
 * This program tests  Petersons solution to the critical section problem.
 *
 */


public class AlgorithmFactory
{
   public static void main(String args[]) {

    MutualExclusion algorithm = new Petersons();

	Thread first = new Thread(new Worker("Worker 0", 0, algorithm));
	Thread second = new Thread(new Worker("Worker 1", 1, algorithm));

      first.start();
      second.start();
   }
}
