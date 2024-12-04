#include <vector>
#include <tuple>
#include <array>
#include <string>
#include <fstream>
#include <iostream>

std::vector<std::string> readFile(const std::string& filename) {
    std::vector<std::string> data;
    std::ifstream file(filename);
    std::string line;

    if (!file.is_open()) {
        std::cerr << "Error: Could not open file" << std::endl;
        exit(1);
    }
    
    while (std::getline(file, line))
        data.push_back(line);

    file.close();
    return data;
}

bool isInRange(int x, int y, std::vector<std::string> data) {
    return y >= 0 && y < data.size() && \
           x >= 0 && x < data[y].length();
}

// PART 1

std::vector<std::tuple<int, int>> directions_part_1 = {
    {-1, -1}, {+0, -1}, {+1, -1},
    {-1, +0},           {+1, +0},
    {-1, +1}, {+0, +1}, {+1, +1}
};

int checkXMas(int y, int x, int count, std::vector<std::string> data) {
    std::string str = "XMAS";

    for (const auto& [dx, dy] : directions_part_1) {
        int tmpX = x;
        int tmpY = y;
        for (size_t i = 0; i < str.length(); i++) {
            if (!isInRange(tmpX, tmpY, data) || !(str[i] == data[tmpY][tmpX]))
                break;
            tmpX += dx;
            tmpY += dy;
            if (i == str.length() - 1)
                count++;
        }
    }
    return count;
}

// PART 2

std::vector<std::tuple<int, int>> directions_part_2 = {
    {-1, -1}, {+1, -1},
    {-1, +1}, {+1, +1}
};

int checkX_Mas(int y, int x, int count, std::vector<std::string> data) {
    if (data[y][x] != 'A')
        return count;

    int matches = 0;
    for (const auto& [dx, dy] : directions_part_2) {
        if (isInRange(x + dx, y + dy, data) && data[y + dy][x + dx] == 'S' && \
            isInRange(x - dx, y - dy, data) && data[y - dy][x - dx] == 'M')
                    matches++;
    }

    if (matches == 2)
        count++;

    return count;
}

int main() {
    std::vector<std::string> data = readFile("input.txt");
    int count_part_1 = 0;
    int count_part_2 = 0;

    for (size_t y = 0; y < data.size(); y++) {
        for (size_t x = 0; x < data[y].length(); x++) {
            count_part_1 = checkXMas(y, x, count_part_1, data);
            count_part_2 = checkX_Mas(y, x, count_part_2, data);
        }
    }

    std::cout << "#1 -> " << count_part_1 << std::endl;
    std::cout << "#2 -> " << count_part_2 << std::endl;
}