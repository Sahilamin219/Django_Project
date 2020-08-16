#include <bits/stdc++.h>
#define sz(a) int(a.size())
#define f(i,a,b) for(long long int i=a;i<b;i++)
#define r(i,a,b) for(long long int i=a;i>b;i--) 
#define pb push_back
#define mkp make_pair
#define mod 1000000007;
#define all(x) x.begin(), x.end()
using namespace std;
typedef long long int ll;
int main(){
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    int t;cin>>t;
    while(t--)
    {
        string a,b;
        cin>>a>>b;
        sort(all(a));
        do{
            int i=0,j=0;
            while(i<sz(b) and j<sz(a))
            {
                if(a[j]==b[i])
                {
                    j++;i++;
                }
                else
                {
                    j++;
                }
            }
            if(i==sz(a)){break;}
        }while(next_permutation(all(a)));
        cout<<a<<endl;
    }
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    return 0;
}