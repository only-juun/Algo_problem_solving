import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Main {
    static int n, m;
    static int[] nums;
    static Set<String> seq = new HashSet<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        nums = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(nums);
        choose(0, new int[m], 0, bw);

        bw.flush();
        bw.close();
        br.close();
    }

    static void choose(int cur, int[] arr, int start, BufferedWriter bw) throws IOException {
        if (cur == m) {
            String s = Arrays.toString(arr).replaceAll("[\\[\\],]", "");
            if (!seq.contains(s)) {
                seq.add(s);
                bw.write(s + "\n");
            }
            return;
        }

        for (int i = start; i < n; i++) {
            arr[cur] = nums[i];
            choose(cur + 1, arr, i, bw);
        }
    }
}