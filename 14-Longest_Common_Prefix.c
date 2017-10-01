char* longestCommonPrefix(char** strs, int strsSize) {
    int i, k, len1;
    static char res[1000];

    if(strsSize == 0)   return "";

    strcpy(res,strs[0]);

    for(i = 1; i < strsSize; i++) {
        len1 = strlen(res);

        k = 0;
        while(k < len1) {
            if(res[k] != strs[i][k]){
                res[k] = '\0';
                break;
            }
            k++;
        }
    }

    return res;
}