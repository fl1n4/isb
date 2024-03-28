#include <iostream>
#include <random>
#include <sstream>

const int SIZE = 128;
using namespace std;

string generateRandomSequence() {
    string sequence;
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(0, 1);

    for (int i = 0; i < SIZE; ++i) {
        stringstream ss;
        ss << dis(gen);
        sequence += ss.str();
    }

    return sequence;
}

int main() {
    string randomSequence = generateRandomSequence();
    cout << "Generated Sequence: " << randomSequence << endl;

    return 0;
}