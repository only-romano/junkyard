function pow(x, n) {
    if (n == 1) {
        return x;
    }

    let result = x * pow(x, n-1);
    return result;
}