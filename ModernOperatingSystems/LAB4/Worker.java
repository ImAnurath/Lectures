/**
 * Worker.java
 *
 * This is a thread that is used to demonstrate solutions
 * to the critical section problem.
 */


public class Worker implements Runnable
{
	private String name;
	private int id;
   	private MutualExclusion mutex;

   public Worker(String name, int id, MutualExclusion mutex) {
      this.name = name;
      this.id = id;
      this.mutex = mutex;
   }

   public void run() {
      while (true) {
         mutex.entrySection(id);
         MutualExclusionUtilities.criticalSection(name);
         mutex.exitSection(id);
         MutualExclusionUtilities.nonCriticalSection(name);
      }
   }


}
