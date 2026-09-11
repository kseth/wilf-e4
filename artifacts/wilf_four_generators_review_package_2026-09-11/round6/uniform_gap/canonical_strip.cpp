// Export every corner result from the previously audited exact unit DP.
#define main previous_driver_main
#include "../../round5/weighted_analytic/one_corner/one_corner_unit_dp.cpp"
#undef main
int main() {
  for(int R=18; R<=21; ++R)
    for(int a=1; 3*a<=R+1; ++a)
      for(int b=a; a+2*b<=R+1; ++b)
        for(int c=b; a+b+c<=R+1; ++c) {
          auto v=solve(R,4,{a,b,c});
          std::cout << R << " " << a << " " << b << " " << c << " " << v.score << "\n";
        }
}
