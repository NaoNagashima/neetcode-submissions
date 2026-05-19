class Solution {
    public String mergeAlternately(String word1, String word2) {
        int index = 0;
        int minLen = Math.min(word1.length(), word2.length());

        String result = "";

        while(index < minLen){
            System.out.println(result);
            result = result + word1.charAt(index) + word2.charAt(index);
            index++;
        }

        if (word1.length() == minLen){
            return result + word2.substring(index);
        }
        return result + word1.substring(index);
    }
}