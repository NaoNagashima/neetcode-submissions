class Solution {
    public boolean validPalindrome(String s) {
        int first = 0;
        int last = s.length()-1;
        boolean deletedOne = false;

        while (first < last){
            if (s.charAt(first) != s.charAt(last)){
                return isPalindrome(s.substring(0,first)+s.substring(first+1)) || isPalindrome(s.substring(0,last)+s.substring(last+1));
            }
            first++;
            last--;
        }
        return true;
    }

    private boolean isPalindrome(String s){
        int first = 0;
        int last = s.length() - 1;

        while(first < last){
            if (s.charAt(first) != s.charAt(last)){
                return false;
            }
            first++;
            last--;
        }
        return true;
    }
}