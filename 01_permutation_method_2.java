import java.util.*;

class PermutationsMethod2{
	public static void permutations(String s){
		permutations("", s);
	}

	private static void permutations(String prefix, String suffix){
		if(suffix.length() == 0){
			System.out.println(prefix);
		}else{
			for(int i = 0; i < suffix.length(); i++){
				permutations(prefix + suffix.charAt(i), suffix.substring(0, i) + suffix.substring(i+1, suffix.length())); 
			}
		}
	}

	public static void main(String[] args) {
		permutations("abcd");
	}
}