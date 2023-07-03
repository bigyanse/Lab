import java.rmi.Naming;
import java.util.Scanner;

public class RmiClient {
	public static void main(String args[]) {
		try {
			RmiServerIntf obj = (RmiServerIntf) Naming.lookup("//localhost/CalculatorService");
			Scanner scanner = new Scanner(System.in);

			System.out.print("Enter the first number: ");
			int a = scanner.nextInt();

			System.out.print("Enter the second number: ");
			int b = scanner.nextInt();

			System.out.println("Addition Result: " + obj.add(a, b));
			System.out.println("Subtraction Result: " + obj.sub(a, b));
			System.out.println("Multiply Result: " + obj.mul(a, b));

			try{
				System.out.println("Division Result: " + obj.div(a, b));
			} catch(Exception e) {
				System.err.println("Division Error: " + e.getMessage());
				e.printStackTrace();
			}
		} catch(Exception e) {
				System.err.println("RMI Client Exception: " + e.getMessage());
				e.printStackTrace();
		}
	}
}
