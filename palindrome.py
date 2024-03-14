class Solution {
public:
bool isPalindrome(int x) {
    if (x < 0 || (x % 10 == 0 && x != 0)) {
        return false;
    }

    long long reversedNum = 0;
    int originalNum = x;

    while (x > 0) {
        int lastDigit = x % 10;
        reversedNum = reversedNum * 10 + lastDigit;
        x /= 10;
    }

    return reversedNum == originalNum;
}
        
};
