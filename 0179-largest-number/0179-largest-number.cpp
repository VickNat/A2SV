bool c_comparator(string a, string b){
        if(a+b>b+a)return true;
        return false;
    }
class Solution {
public:
    string largestNumber(vector<int>& nums) {
        string ans;
        vector<string> A_str;
        int start=0;

        for(int i:nums){
            A_str.push_back(to_string(i));
        }

        sort(A_str.begin(), A_str.end(), c_comparator);

        for(string x: A_str){
            ans+=x;
        }

        while(ans[start]=='0' && start<ans.size()-1)
            start++;
        return ans.substr(start);
    }
};