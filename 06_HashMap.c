#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct LinkedList{
	char * name; // This is the data we want to access
	int age;
	struct LinkedList* next;
};

typedef struct LinkedList* node;

node createNode(){
	node temp;
	temp = (node)malloc(sizeof(struct LinkedList));
	temp->next = NULL;
	return temp;
}

void append(node head, char * name, int age){
	node temp, current_node;
	temp = createNode();
	temp->name = name;
	temp->age = age;

	if(head == NULL){
		head = temp;
	}else{
		current_node = head;

		while(current_node->next != NULL){
			current_node = current_node->next;
		}
		current_node->next = temp;
	}
}

int search(node head, char * name){
	node current_node = head;
	// printf("Head is: %s\n", current_node->name);
	while(current_node != NULL){
		// printf("%s\n", current_node->name);
		if(strcmp(current_node->name, name) == 0 ){
			// printf("Found!\n");
			return current_node->age;
		}
		current_node = current_node->next;
	}

	return -1;
}

void display(node head){
	node current_node;
	int index = 0;

	if(head == NULL){
		return;
	}else{
		current_node = head;

		while(current_node->next != NULL){
			current_node = current_node->next;
			printf("%d: %s\n", index, current_node->name);
			index++;
		}
	}

}

int hash_function(char * string){
	unsigned int sum = 0;
	for(int i = 0; i < strlen(string); i++){
		sum += (int) string[i];
	}
	// printf("Hash: %d\n", sum);
	return sum % 100;
}

void insert(node arr[100], char * name, int age){

	node temp = createNode();
	temp->name=name;
	temp->age=age;
	int hash = hash_function(name);
	if(arr[hash] == NULL){
		arr[hash] = temp;
		// printf("New node.\n");
	}else{
		node current_node = arr[hash];

		while(current_node->next != NULL){
			current_node = current_node->next;
		}

		current_node->next=temp;
		// printf("New.\n");
	}
}

int get(node arr[100], char * name){
	// printf("Hash for %s is: %d\n", name, hash_function(name));
	int hash = hash_function(name);
	if(arr[hash] != NULL){
		return search(arr[hash], name);
	}
}

int main(){
	// node my_node = createNode();
	// append(my_node,"Lona");
	// append(my_node,"Graig");
	// append(my_node,"Angel");
	// append(my_node,"Kendall");
	// append(my_node,"Riley");

	// display(my_node);

	node arr[100];
	for(int i = 0; i < sizeof(arr)/sizeof(node);i++){
		arr[i] = NULL;
	}

	insert(arr, "Garry", 23);	
	insert(arr, "Ladawn", 23);	
	insert(arr, "Cordie", 63);	
	insert(arr, "Stasia", 25);	
	insert(arr, "Lavada", 27);	
	insert(arr, "Fletcher", 70);	
	insert(arr, "Mikaela", 20);	
	insert(arr, "Latoyia", 66);	
	insert(arr, "Houston", 29);	
	insert(arr, "Kacie", 62);	
	insert(arr, "Cherri", 25);	
	insert(arr, "Rufus", 47);	
	insert(arr, "Elke", 62);	
	insert(arr, "Garnett", 44);	
	insert(arr, "Eufemia", 39);	
		insert(arr, "aabb", 41);	
	insert(arr, "baab", 42);	
	insert(arr, "abab", 43);	
	insert(arr, "baba", 44);


	int age = get(arr, "baab");
	printf("Houston's age is: %d: \n", age);
	return 0;
}
