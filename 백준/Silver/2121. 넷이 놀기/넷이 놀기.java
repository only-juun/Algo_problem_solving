import java.io.*;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
    static class Pair {
        int x, y;

        Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Pair pair = (Pair) o;
            return x == pair.x && y == pair.y;
        }

        @Override
        public int hashCode() {
            return 31 * x + y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        HashSet<Pair> pos = new HashSet<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            pos.add(new Pair(x, y));
        }

        System.out.println(countPossibleRectangles(pos, a, b));
    }

    private static boolean isPossible(HashSet<Pair> pos, int x, int y, int a, int b) {
        return pos.contains(new Pair(x + a, y + b)) && pos.contains(new Pair(x + a, y)) && pos.contains(new Pair(x, y + b));
    }

    private static int countPossibleRectangles(HashSet<Pair> pos, int a, int b) {
        int ans = 0;
        for (Pair p : pos) {
            if (isPossible(pos, p.x, p.y, a, b)) {
                ans++;
            }
        }
        return ans;
    }
}
