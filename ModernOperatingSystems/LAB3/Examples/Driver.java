package Examples;
public class Driver
{
	public static void main(String[] args) {
	 if (args.length > 0) {
	  if (Integer.parseInt(args[0]) < 0)
	   System.err.println(args[0] + " must be >= 0.");
	  else {
	   Sum sumObject = new Sum();
	   int upper = Integer.parseInt(args[0]);
	   Thread thrd = new Thread(new Summation(upper, sumObject));
	   thrd.start();
	   try {
	     thrd.join();
	     System.out.println
		("The sum of "+upper+" is "+sumObject.getSum());
	  } catch (InterruptedException ie) { }
	 }
	}
	else
	 System.err.println("Usage: Summation <integer value>"); }
}