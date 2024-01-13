class Solution {
public:
    int minSteps(string s, string t) {
        map<int,int> mp;
        int k=0,ans=0;
        for(int i=0;i<s.size();i++)
        {
            mp[s[i] - 'a']++;
            mp[t[i] - 'a']--;
        }
        // for(int i=0;i<26;i++)
        // {
        //     ans+=mp[i];
        // }
        for ( auto it : mp){ 
            if (it.second < 0) ans += (it.second * -1);
        }

        return ans;
    
    }
};