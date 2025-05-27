/**
 * MutualExclusionUtilities.java
 *
 * Utilities for simulating critical and non-critical sections.
 *
 */

public class MutualExclusionUtilities
{
   /**
    * critical and non-critical sections are simulated by sleeping
    * for a random amount of time between 0 and 3 seconds.
    */
   public static void criticalSection(String name) {
      System.out.println(name + " in critical section");
      SleepUtilities.nap(3);
   }
   
   public static void nonCriticalSection(String name) {
      System.out.println(name + " out of critical section");
      SleepUtilities.nap(3);
   }
}
