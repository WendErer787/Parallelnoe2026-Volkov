#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <filesystem>
#include <string>
#include <iomanip>

std::vector<std::vector<int>> readMatrix(const std::filesystem::path& filepath, int& n) {

    std::vector<std::vector<int>> matrix;

    std::ifstream file(filepath);

    if (!file.is_open()) {
        std::cout << "Error open file: " << filepath << "\n";
        return matrix;
    }

    file >> n;
    matrix.assign(n, std::vector<int>(n, 0));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            file >> matrix[i][j];
        }
    }
    return matrix;
}

void writeMatrix(const std::filesystem::path& filepath,
                 const std::vector<std::vector<int>>& matrix) {

    std::ofstream file(filepath);

    if (!file.is_open()) {
        std::cout << "Error create file: " << filepath << "\n";
        return;
    }

    const int n = static_cast<int>(matrix.size());
    file << n << "\n";

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            file << matrix[i][j];
            if (j + 1 < n) file << ' ';
        }
        file << '\n';
    }
}

std::vector<std::vector<int>> multiply(
        const std::vector<std::vector<int>>& a,
        const std::vector<std::vector<int>>& b) {

    const int n = static_cast<int>(a.size());
    std::vector<std::vector<int>> c(n, std::vector<int>(n, 0));

    for (int i = 0; i < n; ++i) {
        for (int k = 0; k < n; ++k) {
            const int aik = a[i][k];
            const auto& brow = b[k];
            auto& crow = c[i];
            for (int j = 0; j < n; ++j) {
                crow[j] += aik * brow[j];
            }
        }
    }
    return c;
}

int main() {

    const std::string s = "2000";   // размер матрицы, меняется вручную

    int n = 0;

    auto a = readMatrix("data/A" + s + ".txt", n);
    auto b = readMatrix("data/B" + s + ".txt", n);

    if (a.size() != b.size() || a.empty() || b.empty()) {
        std::cout << "Size matrix don't saim or not-create\n";
        return 1;
    }

    const auto start = std::chrono::high_resolution_clock::now();
    auto c = multiply(a, b);
    const auto end = std::chrono::high_resolution_clock::now();

    writeMatrix("data/C" + s + ".txt", c);

    const double ms =
        std::chrono::duration<double, std::milli>(end - start).count();

    std::cout << "Size: " << n << "x" << n << "\n";
    std::cout << "Time: " << std::fixed << std::setprecision(3) << ms << " ms\n";

    return 0;
}