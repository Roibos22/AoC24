#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

int main() {
	int distance = 0;
	std::ifstream inputFile("input.txt");
	std::string line;
	std::vector<int> leftList;
	std::vector<int> rightList;

	if (!inputFile.is_open()) {
		std::cerr << "Error: could not open file" << std::endl;
		exit(1);
	}
	while (std::getline(inputFile, line)) {
		int leftNum, rightNum;
		std::stringstream ss(line);
		if (ss >> leftNum >> rightNum) {
			leftList.push_back(leftNum);
			rightList.push_back(rightNum);
		}
	}

	// PART 1

	sort(leftList.begin(), leftList.end());
	sort(rightList.begin(), rightList.end());

	for(int i = 0; i < leftList.size(); i++)
		distance += abs(leftList[i] - rightList[i]);

	std::cout << "#1 -> " << distance << std::endl;

	// PART 2

	int similarityScore = 0;

	for(int i = 0; i < leftList.size(); i++)
		similarityScore += leftList[i] * std::count(rightList.begin(), rightList.end(), leftList[i]);
	
	std::cout << "#2 -> " << similarityScore << std::endl;
}




