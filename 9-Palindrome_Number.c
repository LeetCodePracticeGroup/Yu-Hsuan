/* The compiler needs to cupport C99 and include <stdbool.h> to use 'bool' */

bool isPalindrome(int x) {
    char x_str[12];
    int x_rev = 0, x_copy;

    sprintf(x_str, "%d", x);

    if (x_str[0] == '-') {
        return false;
    }

    x_copy = x;
    while (x != 0){
        x_rev = x_rev * 10 + x % 10;
        x = x / 10;
    }

    if (x_rev == x_copy)    return true;
    else    return false;    
}