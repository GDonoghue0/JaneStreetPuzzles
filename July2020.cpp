#include <iostream>
#include <fstream>
#include <cmath>

long long tern2dec(int* tern, unsigned int length)
{
  long long dec = 0;
  for (unsigned int idx = 0; idx < length; ++idx) {
    dec += tern[idx]*pow(4,length-idx-1);
  }
  return dec;
}

int* construct_ternary_down(int* tern, int level, int max_trits, std::ofstream& file, long long max_search)
{
  if (level > max_trits-1) {
    long long tern_val = tern2dec(tern,max_trits);
    if (tern_val == max_search) {
      for (unsigned int i = 0; i < max_trits; i++) {
        std::cout << (tern[i] == -1 ? "T" : std::to_string(tern[i]));
      }
      std::cout << " " << tern_val << std::endl;
    } else {
      for (unsigned int i = 0; i < max_trits; i++) {
        file << (tern[i] == -1 ? "T" : std::to_string(tern[i]));
      }
      file << " " << tern_val << std::endl;
    }
    if (tern_val < max_search || tern_val < 1) {
      std::exit(0);
      return nullptr;
    }
    return tern;
  }
  for (int i = 1; i >= -1; --i) {
    tern[level] = i;
    construct_ternary_down(tern, level+1, max_trits, file, max_search);
  }
  return tern;
}

int* construct_ternary_up(int* tern, int level, int max_trits, std::ofstream& file, long long max_search)
{
  if (level == max_trits) {
    long long tern_val = tern2dec(tern,max_trits);
    if (tern_val == max_search) {
      for (unsigned int i = 0; i < max_trits; i++) {
        std::cout << (tern[i] == -1 ? "T" : std::to_string(tern[i]));
      }
      std::cout << " " << tern_val << std::endl;
    } else {
      for (unsigned int i = 0; i < max_trits; i++) {
        file << (tern[i] == -1 ? "T" : std::to_string(tern[i]));
      }
      file << " " << tern_val << std::endl;
    }
    if (tern_val > max_search || tern_val < 1) {
      std::exit(0);
      return nullptr;
    }
    return tern;
  }
  for (int i = -1; i <= 1; ++i) {
    tern[level] = i;
    construct_ternary_up(tern, level+1, max_trits, file, max_search);
  }
  return tern;
}

int main(){
  int max_trits = 27;
  int tern[28];
  tern[0] = 1;
  for (unsigned int i = 1; i < max_trits+1; ++i) {
    tern[i] = -1;
  }
  std::ofstream file;
  file.open("temp.txt");
  construct_ternary_up(tern, 1, max_trits, file, 3002419186324481);
  file.close();
  return 0;
}
