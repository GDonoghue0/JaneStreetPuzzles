#include <vector>
#include <armadillo>
#include <cassert>

class Grid{
public:
  Grid(const unsigned int N_in, const unsigned int select = 0) 
    : N(N_in)
  {
    M.resize(N,N);
    M.zeros();

    switch (select) {
      case 0:
      M(0,2) = 4, M(1,3) = 6, M(2,0) = 5, M(3,1) = 3, M(3,5) = 6, M(4,6) = 2, M(5,3) = 1, M(6,4) = 4;
      left = {5,7,0,0,0,5,7};
      right = {7,4,0,0,0,7,6};
      top = {5,4,0,0,0,7,5};
      bottom = {5,7,0,0,0,3,6};
      break;
      default:
      assert(false);
    }
  }

  void print_grid()
  {
    std::cout << "M = \n" << M << std::endl;
  }

  bool is_full_grid()
  {
    arma::Col<int> counts(N+1, arma::fill::zeros);
    for (unsigned int i = 0; i < N; ++i) {
      for (unsigned int j = 0; j < N; ++j) {
        counts(M(i,j))++;
      }
    }
    for (unsigned int i = 1; i <= N; ++i) {
      if (counts(i) != i) {
        return false;
      }
    }
    return true;
  }

  bool has_four_per_rowcol()
  {
    for (unsigned int i = 0; i < N; ++i) {
      arma::Col<int> non_zeros = arma::nonzeros(M.col(i));
      if (non_zeros.n_elem != 4) {
        return false;
      }
    }
    for (unsigned int i = 0; i < N; ++i) {
      arma::Col<int> non_zeros = arma::nonzeros(M.row(i));
      if (non_zeros.n_elem != 4) {
        return false;
      }
    }
    return true;
  }

  bool sums_rowcols_to_twenty()
  {
    arma::Row<int> row_sum = sum(M,0);
    arma::Col<int> col_sum = sum(M,1);
    return arma::all(row_sum == 20) && arma::all(col_sum == 20);
  }

  bool is_connected()
  {
    return false;
  }

  bool is_sparse()
  {
    for (unsigned int i = 0; i < N-1; ++i) {
      for (unsigned int j = 0; j < N-1; ++j) {
        if (M(i,j) != 0 && M(i+1,j) != 0 && M(i,j+1) != 0 && M(i+1,j+1) != 0) {
          return false;
        }
      }
    }
    return true;
  }

  bool satisfies_outside_values()
  {
    //left
    unsigned int j = 0;
    for (unsigned int i = 0; i < N; ++i) {
      j = 0;
      while (M(i,j) != left(i) && j < N) {
        j++
      }
      if (j == N) {
        return false;
      }
    }
  }


private:
  unsigned int N;
  arma::Mat<int> M;
  arma::Col<int> left;
  arma::Col<int> right;
  arma::Row<int> top;
  arma::Row<int> bottom;

};

int main(){

  const unsigned int N = 7;
  Grid grid(N);
  grid.print_grid();
  grid.is_full_grid();
  grid.has_four_per_rowcol();
  grid.sums_rowcols_to_twenty();
  grid.is_sparse();


  return 0;
}