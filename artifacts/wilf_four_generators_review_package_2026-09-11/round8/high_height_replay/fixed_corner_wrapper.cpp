#define main independent_all_corners_main
#include "independent_specialized_piece_worker.cpp"
#undef main
int main(){I q;V lo,hi;std::array<int,3>p;while(std::cin>>q>>lo[0]>>lo[1]>>lo[2]>>hi[0]>>hi[1]>>hi[2]>>p[0]>>p[1]>>p[2]) std::cout<<solve(q,lo,hi,p)<<'\n'<<std::flush;}
