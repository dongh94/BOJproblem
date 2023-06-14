package kdh.opentutorials.javatutorials.loop;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 스티커붙이기 {
    static int N, M, K;
    static int[][] notebook;
    static int answer;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        notebook = new int[N][M];

        for (int i = 0; i < K; i++) {
            // 입력
            String str1 = br.readLine();
            st = new StringTokenizer(str1);
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int[][] stickerBoard = new int[r][c];
            // 초기 스티커
            for (int y = 0; y < r; y++) {
                st = new StringTokenizer(br.readLine());
                for (int x = 0; x < c; x++) {
                    stickerBoard[y][x] = Integer.parseInt(st.nextToken());
                }
            }
            // 붙일 건데, 4번 돌리는게 제일 먼 loop
            int rotate_cnt = 0;
            while (rotate_cnt < 4) {
                if (attach(stickerBoard))
                    break;
                stickerBoard = rotate(stickerBoard);
                rotate_cnt++;

                }
            }
        System.out.println(answer);

        }

    static int[][] rotate(int[][] stickerBoard) {
        int[][] newStickerBoard = new int[stickerBoard[0].length][stickerBoard.length];
        for (int r = 0; r < stickerBoard.length; r++) {
            for (int c = 0; c < stickerBoard[r].length; c++) {
                newStickerBoard[c][stickerBoard.length - 1 - r] = stickerBoard[r][c];
            }
        }


        return newStickerBoard;
    }

    static boolean attach(int[][] stickerBoard) {
        for (int i = 0; i < N - stickerBoard.length + 1; i++) {
            for (int j = 0; j < M - stickerBoard[0].length + 1; j++) {
                if (check(stickerBoard, i, j)) {
                    attachOne(stickerBoard, i, j);
                    return true;
                }
            }
        }
        return false;
    }

    private static void attachOne(int[][] stickerBoard, int i, int j) {
        for (int r = 0; r < stickerBoard.length; r++) {
            for (int c = 0; c < stickerBoard[r].length; c++) {
                if (stickerBoard[r][c] == 1) {
                    notebook[r + i][c + j] = 1;
                    answer++;
                }
            }
        }
    }

    private static boolean check(int[][] stickerBoard, int i, int j) {
        for (int r = 0; r < stickerBoard.length; r++) {
            for (int c = 0; c < stickerBoard[r].length; c++) {
                if (stickerBoard[r][c] == 1 && notebook[r + i][c + j] == 1) {
                    return false;
                }
            }
        }
        return true;
    }

}

