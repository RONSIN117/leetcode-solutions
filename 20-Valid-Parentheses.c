#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

bool isValid(char* s) {
    int len = strlen(s);
    
    // An odd length string can never be valid
    if (len % 2 != 0) {
        return false;
    }

    char* stack = (char*)malloc(len * sizeof(char));
    int top = -1;

    for (int i = 0; i < len; i++) {
        char c = s[i];
        
        if (c == '(' || c == '{' || c == '[') {
            stack[++top] = c;
        } else {
            // If we have a closing bracket but stack is empty
            if (top == -1) {
                free(stack);
                return false;
            }
            
            char open = stack[top--];
            if ((c == ')' && open != '(') ||
                (c == '}' && open != '{') ||
                (c == ']' && open != '[')) {
                free(stack);
                return false;
            }
        }
    }

    // If stack is empty, all brackets were matched correctly
    bool result = (top == -1);
    free(stack);
    
    return result;
}