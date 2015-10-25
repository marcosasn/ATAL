package exemplos;

import java.util.ArrayList;
import java.util.List;

public class ProblemaMochila {

	public static Integer[][] inicializaMatriz(Integer [][] array) {
		for (int i = 0; i < array.length; i++) {
			for (int j = 0; j < array[0].length; j++) {
				if (i == 0 || j == 0){
					array[i][j] = 0;
				}
			}
		}
		return array;
	}
	
	public static Integer[][] MochilaProgramacaoDinamica(Integer[]v, Integer[]w, Integer W){
		Integer[][] V = new Integer[v.length+1][W+1];
		V = inicializaMatriz(V);
		
		for (int i = 1; i <= v.length; i++) {
			for (int j = 1; j <= W; j++) {
				if(w[i-1] > j){
					V[i][j] = V[i-1][j];
				}
				else{
					V[i][j] = max(V[i-1][j], V[i-1][j-w[i-1]] + v[i-1]);
				}
			}		
		}
		return V;
	}
	
	public static List<Integer> Reconstrucao(Integer[]v, Integer[]w, Integer W, Integer[][] V){
		List<Integer> S = new ArrayList<Integer>();
		int i = v.length;
		int j = W;
		
		while(i >= 1){
			if (w[i-1] <= j && V[i-1][j] < V[i-1][j-w[i-1]] + v[i-1]){
				S.add(i);
				j = j-w[i-1];
			}
			i = i-1;
		}
		return S;
	}
	
	
	private static int max(int x, int y) {
		if (x >= y){
			return x;
		}
		return y;
	}
	
	public static void main(String[] args) {
		Integer[]v = {12,10,20,15};
		Integer[]w = {2,1,3,2}; 
		Integer W = 5;
		
		Integer[][] V = MochilaProgramacaoDinamica(v, w, W);
		Integer result = V[v.length][W];
		
		System.out.println(result);
		System.out.println(Reconstrucao(v, w, W, V));
	}
}