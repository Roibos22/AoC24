#include <fstream>
#include <string>
#include <sstream>
#include <iostream>
#include <regex>

int MAX_LENGHT = 42;
bool enabled = true;
std::regex pattern_mul(R"(^mul\((\d+),(\d+)\))");
std::regex pattern_do(R"(^do\(\))");
std::regex pattern_dont(R"(^don\'t\(\))");

std::string readFile(const std::string& filename) {
	std::ifstream file(filename);
	std::stringstream buffer;
	buffer << file.rdbuf();
	return buffer.str();
}

int isMul(const std::string& input, size_t pos) {
	std::smatch match;

	if (std::regex_search(input.begin() + pos, input.begin() + pos + MAX_LENGHT, match, pattern_mul))
		return std::stoi(match[1]) * std::stoi(match[2]);
	return 0;
}


bool check_enabled(const std::string& input, size_t pos) {
	std::smatch match_do;
	std::smatch match_dont;

	if (std::regex_search(input.begin() + pos, input.begin() + pos + MAX_LENGHT, match_do, pattern_do))
		return true;
	if (std::regex_search(input.begin() + pos, input.begin() + pos + MAX_LENGHT, match_dont, pattern_dont))
		return false;
	return enabled;
}

int main() {
	int res1 = 0;
	int res2 = 0;
	std::string input = readFile("input.txt");

	for (int i = 0; i < input.length(); i++) {
		res1 += isMul(input, i);
		enabled = check_enabled(input, i);
		if (enabled)
			res2 += isMul(input, i);
	}

	std::cout << "#1 -> " << res1 << std::endl;
	std::cout << "#2 -> " << res2 << std::endl;
}