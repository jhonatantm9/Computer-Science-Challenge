class Solution {
public:
    int longestValidParentheses(string s) {
        stack<pair<char,int>> parenthesis;
        for(int i = 0; i < s.length(); i++){
            char p = s[i];
            if(p == '('){
                parenthesis.push(make_pair('(', i));
            }else{
                if(!parenthesis.empty() && parenthesis.top().first == '('){
                    parenthesis.pop();
                }else{
                    parenthesis.push(make_pair(')', i));
                }
            }
        }
        if(parenthesis.empty()) return s.length();
        int maxLen = 0, top = s.length();
        while(!parenthesis.empty()){
            int lastIndex = parenthesis.top().second;
            parenthesis.pop();
            maxLen = max(maxLen, (top - lastIndex - 1));
            top = lastIndex;
        }
        maxLen = max(maxLen, top);
        return maxLen;
    }
};