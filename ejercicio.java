import java.util.Arrays;
import java.util.Scanner;

public class ejercicio {
    static int maxn = 100000 + 10;
    int s, n, T;
    int p[] = new int[maxn];
    int c[] = new int[maxn];// C is equivalent to the record array of the sliding window
    boolean flag[] = new boolean[maxn];
    Scanner sc = new Scanner(System.in);
 
    public ejercicio() {
        T = sc.nextInt();
        while (T>0) {
            init();
            System.out.println(this.solve());
            T--;
        }
    }

    public static void main(String[] args) {
        new ejercicio();
    }

    public void init() {
        Arrays.fill(flag, false);
        Arrays.fill(c, 0);
        int re = 0;
        s = sc.nextInt();
        n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            p[i] = sc.nextInt();
            if (i < s) {
                if (c[p[i]]==1)
                    re++;
                c[p[i]]++;
            }
        }

        for (int i = 0; i < n; i++) {
            if (re == 0)
                flag[i] = true;

            if (c[p[i]] == 2)
                re--;
            c[p[i]]--;

            int k = i + s;// represents window sliding
            if (k >= n)
                continue;
            if (c[p[k]]==1||c[p[k]]==2)
                re++;
            c[p[k]]++;
        }
    }

    public boolean judge(int x) {
        for (int i = x; i < n; i += s)
            if (!flag[i])
                return false;
        return true;
    }

    public int solve() {
        int ans = 0;
        //Arrays.fill(c, 0);// Note that the C array should be restored in time
        for (int i = 0; i < s; i++) {
            if (judge(i))
                ans++;
            if (i >= n)
                continue;
            if (c[p[i]]==1 )
                break;// If there is a repetition in the first S, it must be divided.
            c[p[i]]++;
        }
        return ans;
    }
}
