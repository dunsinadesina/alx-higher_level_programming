#include <stdio.h>
#include <stdlib.h>

/* Define the structure for a node in the singly linked list */
typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

/* Function to reverse a linked list */
listint_t *reverse(listint_t *head) {
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next = NULL;

    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}

/* Function to check if a linked list is a palindrome */
int is_palindrome(listint_t **head) {
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *second_half = NULL;
    listint_t *prev_of_slow = *head;
    listint_t *mid_node = NULL;
    int is_pal = 1;

    if (*head != NULL && (*head)->next != NULL) {
        while (fast != NULL && fast->next != NULL) {
            fast = fast->next->next;
            prev_of_slow = slow;
            slow = slow->next;
        }

        if (fast != NULL) {
            mid_node = slow;
            slow = slow->next;
        }

        second_half = slow;
        prev_of_slow->next = NULL;
        second_half = reverse(second_half);

        listint_t *temp1 = *head;
        listint_t *temp2 = second_half;

        while (temp1 != NULL && temp2 != NULL) {
            if (temp1->n != temp2->n) {
                is_pal = 0;
                break;
            }
            temp1 = temp1->next;
            temp2 = temp2->next;
        }

        second_half = reverse(second_half);

        if (mid_node != NULL) {
            prev_of_slow->next = mid_node;
            mid_node->next = second_half;
        } else {
            prev_of_slow->next = second_half;
        }
    }
    return is_pal;
}

/* Function to print the linked list elements */
void print_list(listint_t *node) {
    while (node != NULL) {
        printf("%d ", node->n);
        node = node->next;
    }
    printf("\n");
}

/* Function to create a new node */
listint_t *new_node(int key) {
    listint_t *temp = (listint_t *)malloc(sizeof(listint_t));
    temp->n = key;
    temp->next = NULL;
    return temp;
}

/* Driver code to test the functions */
int main() {
    listint_t *head = new_node(1);
    head->next = new_node(2);
    head->next->next = new_node(3);
    head->next->next->next = new_node(2);
    head->next->next->next->next = new_node(1);

    printf("Linked list: ");
    print_list(head);

    if (is_palindrome(&head)printf("The linked list is a palindrome.\n");
	else
	    printf("The linked list is not a palindrome.\n");
	return (0);
}
