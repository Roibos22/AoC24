#include <iostream>
// #include <functional>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

bool isSorted(std::vector<int> nums) {
	if (is_sorted(nums.begin(), nums.end(), std::less<int>()))
		return true;
	if (is_sorted(nums.begin(), nums.end(), std::greater<int>()))
		return true;
	return false;
}

bool hasCorrectDifferences(std::vector<int> nums) {
	for (int i = 0; i < nums.size() - 1; i++) {
		if (abs(nums[i] - nums[i + 1]) > 3 || abs(nums[i] - nums[i + 1]) < 1)
			return false;
	}
	return true;
}

int partOne(const std::string& filename) {
	std::ifstream inputFile("input.txt");
	std::string line;
	int	safe_files = 0;

	if (!inputFile.is_open()) {
		std::cerr << "Error: could not open file" << std::endl;
		exit(1);
	}

	while (std::getline(inputFile, line)) {
		std::stringstream ss(line);
		std::vector<int> nums;
		int num;
		while (ss >> num)
			nums.push_back(num);

		if (isSorted(nums) && hasCorrectDifferences(nums))
			safe_files += 1;
	}

	return (safe_files);
}

int partTwo(const std::string& filename) {
	std::ifstream inputFile("input.txt");
	std::string line;
	int	safe_files = 0;

	if (!inputFile.is_open()) {
		std::cerr << "Error: could not open file" << std::endl;
		exit(1);
	}

	while (std::getline(inputFile, line)) {
		std::stringstream ss(line);
		std::vector<int> nums;
		int num;
		while (ss >> num)
			nums.push_back(num);

		for(int i = 0; i < nums.size(); i++) {
			std::vector<int> tmp(nums);
			tmp.erase(tmp.begin() + i);

			if (isSorted(tmp) && hasCorrectDifferences(tmp)) {
				safe_files += 1;
				break;
			}
		}
	}

	return (safe_files);
}

int main() {
	std::cout << "#1 -> " << partOne("input.txt") << std::endl;
	std::cout << "#2 -> " << partTwo("input.txt") << std::endl;
}