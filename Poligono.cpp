#include <bits/stdc++.h>

using namespace std;

int const N = 1e4 + 1;
int n, a[N], sum;
set<int> st;

int main() {
  while(scanf("%d", &n) && n != 0) {
    sum = 0;
    st.clear();

    for(int i = 0; i < n; ++i) {
      scanf("%d", a + i);
      sum += a[i];
      
      st.insert(sum);
    }
    cout<<" valor de la suma "<<sum<<endl;
    int res = -1;
    for(int i = n, side; i >= 3 && res == -1; --i) {
      if(sum % i == 0) {

        side = sum / i;
        cout<<"tamano "<<side<<endl;
        cout<<"valor de i "<<i<<endl;
        for(int j = 0, s = 0; s <= side; s += a[j], ++j) {
          bool ok = true;
          cout<<"valor s "<<side<<endl;
          for(int k = s; k < sum && ok; k += side)
            ok &= st.count(k);
          if(ok) {
            res = n - i;
            break;
          }
        }
      }
    }
    printf("%d\n", res);
  }

  return 0;
}