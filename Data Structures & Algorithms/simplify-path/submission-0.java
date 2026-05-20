class Solution {
    public String simplifyPath(String path) {
        Stack<String> pathStack = new Stack<String>();
        int index = 0;
        String pathResult = "";

        path = path + "/";

        for (char c: path.toCharArray()){
            if (c == '/'){
                if (pathResult.equals("..")){
                    if (!pathStack.isEmpty()){
                        pathStack.pop();
                    }
                } else if (!pathResult.equals("") && !pathResult.equals(".")){
                    pathStack.push(pathResult);
                }
                pathResult = "";
            } else {
                pathResult = pathResult + c;
            }
        }


        return "/" + String.join("/", pathStack);
    }
}