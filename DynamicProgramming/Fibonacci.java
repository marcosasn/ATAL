package exemplos;
import java.util.ArrayList;
import java.util.List;


public class Fibonacci {
	
	public static int FibonacciExponencial(int n){
		if(n <= 1){
			return n;
		}
		return FibonacciExponencial(n-1)+FibonacciExponencial(n-2);
	}
	
	public static int FibonacciProgramacaoDinamica(int n){
		List<Integer> A = new ArrayList<Integer>();
		A.add(0);
		A.add(1);
		
		for (int i = 2; i <= n; i++) {
			A.add(A.get(i-1)+A.get(i-2));	
		}
		return A.get(A.size()-1);
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		System.out.println(FibonacciExponencial(5));
		System.out.println(FibonacciProgramacaoDinamica(5));
	}

}
