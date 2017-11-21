#include <stdio.h>
#include <stdlib.h>

struct LinkedList{
	int data;
	struct LinkedList* next;
};

typedef struct LinkedList *node;


node createNode(){
	node temp;
	temp = (node)malloc(sizeof(struct LinkedList));
	temp->next = NULL;
	return temp;
}

node append(node head, int data){
	node temp, current_node;
	temp = createNode();
	temp->data = data;

	if(head == NULL){
		head=NULL;
	}else{
		current_node = head;

		while(current_node->next != NULL){
			current_node = current_node->next;
		}

		// We are at the last node in the linked list
		current_node->next = temp;
	}

	return head;
}

void displayList(node head){
	node current_node = head;

	while(current_node->next != NULL){
		current_node = current_node->next;
		printf("%d ", 	current_node->data);
	}
}

int length(node head){
	int index = 0;
	node current_node = head;

	while(current_node->next != NULL){
		current_node = current_node->next;
		index++;
	}

	return index;
}


int main(){

	node head = createNode();

	for(int i = 0; i <= 30; i+=5){
		append(head, i);
	}
	printf("Here is the newly created linked list: [ ");
	displayList(head);
	printf("]\n");

	printf("It is of size: %d\n", length(head));

	return 0;
}   