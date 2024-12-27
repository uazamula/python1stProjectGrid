// згенeровано в ChatGPT на основі коду на Python
// пройшло всі 100% тестів на eolymp з максимальним часом 6 мс,
// тобто в 50 разів швидше, ніж код з такою ж структурою на Python
#include <iostream>
#include <vector>
#include <string>

int main() {
    int n;
    std::cin >> n;

    // Зчитування вхідних даних
    std::vector<std::vector<std::string>> N(n, std::vector<std::string>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            std::cin >> N[i][j];
        }
    }

    int ans = 0;

    // Перша частина: перевірка квадратів
    for (int c = 1; c < n; ++c) {
        int nc = n - c;
        for (int i = 0; i < nc; ++i) {
            int ic = i + c;
            for (int j = 0; j < nc; ++j) {
                int jc = j + c;
                if (N[i][j] == N[i][jc] && N[i][j] == N[ic][jc] && N[i][j] == N[ic][j]) {
                    ans++;
                }
            }
        }
    }

    // Друга частина: перевірка "ромбів"
    for (int r = 1; r < n - 1; ++r) {
        for (int c = 1; c < n; ++c) {
            int nj = n - c;
            int cmr = c - r;
            int cr = c + r;
            for (int i = 0; i < nj - r; ++i) {
                int icr = i + cr;
                int ir = i + r;
                for (int j = r; j < nj; ++j) {
                    if (N[i][j] == N[ir][j + c] && N[i][j] == N[icr][j + cmr] && N[i][j] == N[i + c][j - r]) {
                        ans++;
                    }
                }
            }
        }
    }

    std::cout << ans << std::endl;
    return 0;
}
