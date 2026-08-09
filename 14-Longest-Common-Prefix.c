#include <stdlib.h>
#include <string.h>

char* longestCommonPrefix(char** strs, int strsSize) {
    if (strsSize == 0) {
        char* empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }

    int maxLen = strlen(strs[0]);
    char* prefix = (char*)malloc((maxLen + 1) * sizeof(char));
    strcpy(prefix, strs[0]);

    for (int i = 1; i < strsSize; i++) {
        int j = 0;
        while (prefix[j] != '\0' && strs[i][j] != '\0' && prefix[j] == strs[i][j]) {
            j++;
        }
        prefix[j] = '\0'; 
        
        if (j == 0) {
            break; 
        }
    }

    return prefix;
}