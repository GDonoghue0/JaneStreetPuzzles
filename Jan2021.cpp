#include <iostream>
#include <vector>
#include <cmath>

class ToyBag{
  public:
    ToyBag(const int num_toy_types_in)
    : num_toy_types_(num_toy_types_in),
      total_toys_(num_toy_types_in*(num_toy_types_in+1)/2)
    {
      toys_.resize(total_toys_);
      fill_toy_bag();
    }

    void print_toys()
    {
      for (int i = 0; i < toys_.size(); ++i) {
        std::cout << toys_[i] << " ";
      }
      // std::cout << std::endl;
    }

    void fill_toy_bag()
    {
      for (int i = 0; i < toys_.size(); ++i) {
        toys_[i] = round(sqrt(2*(i+1))+1/2);
      }
    }

    void shuffle_toys()
    {
      std::random_shuffle(toys_.begin(), toys_.end());
      print_toys();
      find_the_one();
    }

    void find_the_one()
    {
      std::vector<int>::iterator it = std::find(toys_.begin(), toys_.end(), 1);
      std::cout << ": " << it - toys_.begin() << std::endl;
      // index_tot += index;
    }

    void count_toys()
    {
      std::vector<int>::iterator it = std::find(toys_.begin(), toys_.end(), 1);
      int cnt = std::count(toys_.begin(), it, 2);

    }

    int get_index_tot()
    {
      return index_tot;
    }


  private:
    std::vector<int> toys_;
    int num_toy_types_;
    int total_toys_;
    int index_tot = 0;
};

int main(int argc, char* argv[]) {
  int num_toy_types;
  if (argc > 1) {
    num_toy_types = atoi(argv[1]);
  } else {
    num_toy_types = 3;
  }

  ToyBag tb(num_toy_types);

  int n_samples = 1e6;
  for (int i = 0; i < n_samples; ++i) {
    tb.shuffle_toys();
    // tb.print_toys();
  }
  std::cout << tb.get_index_tot()/(n_samples+0.0) << ", " << num_toy_types*(num_toy_types+1)/2/2 << std::endl;
  return 0;
}