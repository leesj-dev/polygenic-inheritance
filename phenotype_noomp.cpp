#include <algorithm>
#include <chrono>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>

using namespace std;
using boost::multiprecision::cpp_int;

// generates prime numbers under 100
vector<int> generatePrime(int n) {
  vector<int> primes;
  for (int i = 2; i <= n; i++) {
    bool isPrime = true;
    for (int j = 0; j < primes.size(); j++) {
      if (i % primes[j] == 0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime) {
      primes.push_back(i);
    }
  }
  return primes;
}

// checks if an integer is a prime number
bool chkPrime(vector<int> vec, vector<int> ref) {
  for (int i = 0; i < vec.size(); i++) {
    if (find(ref.begin(), ref.end(), vec[i]) == ref.end()) {
      return false;
    }
  }
  return true;
}

int main() {
  int maxAlleles;
  cout << "Enter the number of alleles: ";
  cin >> maxAlleles;
  auto start = chrono::high_resolution_clock::now();
  vector<int> primes = generatePrime(100);
  vector<cpp_int> row(1, 1);
  vector<vector<int> > rowPrime;

  for (int alleles = 1; alleles <= maxAlleles; alleles++) {
    vector<cpp_int> row1 = row;
    row1.push_back(0);
    row1.push_back(0);
    vector<cpp_int> row2 = row1;
    vector<cpp_int> row3 = row1;
    vector<cpp_int> rowFinal;
    rotate(row2.begin(), row2.end() - 1, row2.end());
    rotate(row3.begin(), row3.end() - 2, row3.end());

    for (int i = 0; i < row1.size(); i++) {
      // making the next row of the trinomial triangle
      rowFinal.push_back(row1[i] + row2[i] + row3[i]);
    }
    row = rowFinal;

    if (alleles == maxAlleles) {
      int middle = (rowFinal.size() - 1) / 2;
      cpp_int maxValue = rowFinal[middle];
      cout << maxValue << " ";
    }

    /* for each number in the row, we will make the number into a string and divide it by 2 letters
    and put it into a vector (splitTwo), starting from the beginning of the string */
    for (int num = 0; num < row.size(); num++) {
      string item = to_string(row[num]);
      vector<int> splitTwo;
      int i = 0;

      if (item.length() % 2 == 0) {
        while (i <= item.length() - 2) {
          splitTwo.push_back(stoi(item.substr(i, 2)));
          i += 2;
        }
      }

      else {
        if (item.length() > 2) {
          while (i <= item.length() - 3) {
            splitTwo.push_back(stoi(item.substr(i, 2)));
            i += 2;
          }
        }
        int last_letter = item[item.length() - 1] - '0';
        splitTwo.push_back(last_letter);
      }

      if (chkPrime(splitTwo, primes) == true) {
        splitTwo.push_back(alleles);
        splitTwo.push_back(num);
        /*
        for (int &i: splitTwo) {
          cout << i << ' ';
        }
        cout << '\n';
        */
        rowPrime.push_back(splitTwo);
      }
    }
  }
  vector<int> sum;
  for (int k = 0; k < rowPrime.size(); k++) {
    sum.push_back(accumulate(begin(rowPrime[k]), end(rowPrime[k]) - 2, 0, plus<int>()));
  }

  int idx = distance(begin(sum), max_element(begin(sum), end(sum)));

  for (int &i : rowPrime[idx]) {
    cout << i << ' ';
  }
  cout << sum[idx] << ' ' << rowPrime.size();

  auto end = chrono::high_resolution_clock::now();
  auto duration = chrono::duration_cast<chrono::microseconds>(end - start);
  cout << "\n" << duration.count() / 1000 << "ms" << endl;

  return 0;
}