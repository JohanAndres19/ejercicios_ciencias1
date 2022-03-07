#include <bits/stdc++.h>
using namespace std;

const int INF = 0x3f3f3f3f;
const int maxn = 100000 + 10;
int s, n, T;
int p[maxn], c[maxn]; //C is equivalent to the record array of the sliding window
bool flag[maxn];

void init()
{
    memset(flag, 0, sizeof(flag)); //Be sure to clear the restore
    memset(c, 0, sizeof(c));
     int tamano = sizeof(p);
    int re = 0;
    scanf("%d %d", &s, &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &p[i]);
        if (i < s)
        { 
            if (c[p[i]])
                re++;
            c[p[i]]++;
        }
    }

    for (int i = 0; i < n; i++)
    {
        if (re == 0)
            flag[i] = true;

        if (c[p[i]] == 2)
            re--;
        c[p[i]]--;

        int k = i + s; //represents window sliding
        if (k >= n)
            continue;
        if (c[p[k]]) 
            cout<<"valor ###"<<c[p[k]]<<endl;
            re++;
        c[p[k]]++;
    }
}

bool judge(int x)
{
    for (int i = x; i < n; i += s)
        if (!flag[i])
            return false;
    return true;
}

int solve()
{
    int ans = 0;
    memset(c, 0, sizeof(c)); //Note that the C array should be restored in time
    for (int i = 0; i < s; i++)
    {
        if (judge(i))
            ans++;
        if (i >= n)
            continue;   
        if (c[p[i]])
            break; //If there is a repetition in the first S, it must be divided.
        c[p[i]]++;
    }
    return ans;
}

int main()
{
    scanf("%d", &T);
    while (T--)
    {
       init();
       printf("%d\n", solve());
    }
    return 0;
}
