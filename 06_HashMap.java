import java.util.*;

class HashThing{
	public static void main(String[] args) {
		HashMap<String, Integer> map = new HashMap<String, Integer>();

		map.put("Julien", 20);
		map.put("Loida",84);
		map.put("Skye",73);
		map.put("Lore",67);
		map.put("Macie",76);
		map.put("Arlyne",73);
		map.put("Madalene",63);
		map.put("John",24);
		map.put("Elvira",54);
		map.put("Rochelle",81);
		map.put("Dorcas",86);
		map.put("Ardelle",86);
		map.put("Ned",33);

		System.out.printf("The size of the map is %d, and Julien is %d years old.\n", map.size(), map.get("Julien"));

		ArrayList<Integer> list = new ArrayList<Integer>();

		for(int i = 0; i < 20; i++){
			list.add(i);
		}
		System.out.printf("The array list is: ");
		for(int i: list){
			System.out.printf("%d ", i);
		}
		System.out.println();
	}
}