int reverse(int x) {
    char x_str[12];
    int is_negative = 0;
    int x_rev = 0;

    sprintf(x_str, "%d", x);

    if (x_str[0] == '-') {
        is_negative = 1;
        x = abs(x);
    }

    while (x != 0){
        if (x_rev > (INT_MAX - x % 10) / 10)   return 0;    /*IMPORTANT: check overflow!!*/
        else
            x_rev = x_rev * 10 + x % 10;
        x = x / 10;
    }

    if (is_negative == 1)    return 0-x_rev;
    else    return x_rev;
}