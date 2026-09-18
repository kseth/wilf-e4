#include <limits>
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <vector>

static_assert(std::numeric_limits<long long>::digits >= 63, "64-bit scores required");
static_assert(std::numeric_limits<int>::digits >= 31, "32-bit indices required");
static_assert(std::numeric_limits<std::uint64_t>::digits == 64, "64-bit bitsets required");

// Finite Lemma 2.2: generator-box enumeration using integer semigroup membership.
// A tuple can be discarded from the counterexample search exactly when
// [B-m+1,B] is not fully contained in S: this is equivalent to max Ap(S,m)>B.

static std::uint64_t window(const std::vector<std::uint64_t>& bits,
                            int start, int width) {
    const std::uint64_t mask = (1ULL << width) - 1;
    if (start <= -width) return 0;
    if (start < 0) return (bits[0] << (-start)) & mask;
    const int block = start / 64, offset = start % 64;
    std::uint64_t result = bits[block] >> offset;
    if (offset) result |= bits[block + 1] << (64 - offset);
    return result & mask;
}

static void mix(std::uint64_t& checksum, std::uint64_t value) {
    for (int k = 0; k < 8; ++k) {
        checksum ^= value & 255;
        checksum *= 1099511628211ULL;
        value >>= 8;
    }
}

static void run(int m) {
    auto start_time = std::chrono::steady_clock::now();
    const int B = m * (m-2);
    const std::uint64_t full = (1ULL << m) - 1;
    std::uint64_t raw = 0, redundant_a = 0, redundant_b = 0;
    std::uint64_t redundant_c = 0, gcd_bad = 0, valid = 0, bounded = 0;
    std::uint64_t negative = 0, zero = 0, checksum = 14695981039346656037ULL;
    int min_w = 1000000000, min_a=0, min_b=0, min_c=0;
    std::vector<unsigned char> ra(B+1), rab(B+1), rabc(B+1);
    std::vector<std::uint64_t> bits((B+1)/64+2);
    for (int a=m+1; a<=B-2; ++a) {
        if (a%m==0) {
            std::uint64_t count=B-a;
            redundant_a+=count*(count-1)/2;
            continue;
        }
        ra[0]=1;
        for (int n=1;n<=B;++n)
            ra[n]=(n>=m && ra[n-m]) || (n>=a && ra[n-a]);
        for (int b=a+1;b<=B-1;++b) {
            if (ra[b]) { redundant_b+=B-b; continue; }
            rab[0]=1;
            std::fill(bits.begin(),bits.end(),0);
            bits[0]=1;
            for (int n=1;n<=B;++n) {
                rab[n]=ra[n] || (n>=b && rab[n-b]);
                if (rab[n]) bits[n/64] |= 1ULL<<(n%64);
            }
            const int g=std::gcd(std::gcd(m,a),b);
            for (int c=b+1;c<=B;++c) {
                if (rab[c]) { ++redundant_c; continue; }
                if (std::gcd(g,c)!=1) { ++gcd_bad; continue; }
                ++valid;
                std::uint64_t reached=0;
                for (int shift=0;shift<=B;shift+=c)
                    reached |= window(bits,B-m+1-shift,m);
                if (reached!=full) continue;
                ++bounded;
                rabc[0]=1;
                int last_gap=-1, genus=0;
                for (int n=1;n<=B;++n) {
                    rabc[n]=rab[n] || (n>=c && rabc[n-c]);
                    if (!rabc[n]) { last_gap=n; ++genus; }
                }
                // Last m values are in S. Closure under +m proves all
                // larger values are in S, so this genus is the full genus.
                const int conductor=last_gap+1;
                const int wilf=3*conductor-4*genus;
                const int M=conductor+m-1;
                const long long sum=1LL*m*genus+1LL*m*(m-1)/2;
                if (M>B) throw std::runtime_error("window equivalence failed");
                if (wilf<0) ++negative;
                if (wilf==0) ++zero;
                if (wilf<min_w) { min_w=wilf;min_a=a;min_b=b;min_c=c; }
                mix(checksum,a);mix(checksum,b);mix(checksum,c);
                mix(checksum,M);mix(checksum,sum);mix(checksum,wilf);
            }
        }
    }
    const std::uint64_t n=B-m;
    raw=n*(n-1)*(n-2)/6;
    if (negative || min_w < 0) throw std::runtime_error("finite predicate failed");
    if(raw!=redundant_a+redundant_b+redundant_c+gcd_bad+valid)
        throw std::runtime_error("count partition failed");
    double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start_time).count();
    std::cout << "{\"m\":"<<m<<",\"generator_bound_inclusive\":"<<B
              <<",\"raw_triples\":"<<raw<<",\"smallest_redundant\":"<<redundant_a
              <<",\"middle_redundant\":"<<redundant_b<<",\"largest_redundant\":"<<redundant_c
              <<",\"nontrivial_gcd\":"<<gcd_bad<<",\"minimal_four_generator_semigroups\":"<<valid
              <<",\"maximum_apery_within_bound\":"<<bounded<<",\"negative_wilf_count\":"<<negative
              <<",\"zero_wilf_count\":"<<zero<<",\"minimum_wilf_with_bounded_apery\":"<<min_w
              <<",\"bounded_minimum_example\":["<<m<<','<<min_a<<','<<min_b<<','<<min_c
              <<"],\"bounded_checksum_fnv1a64\":\""<<checksum<<"\",\"elapsed_seconds\":"<<elapsed<<"}"<<std::endl;
}


int main(int argc, char**) {
    if (argc != 1) { std::cerr << "only complete mode supported\n"; return 2; }
    try { for (int m = 20; m <= 29; ++m) run(m); }
    catch (const std::exception& error) { std::cerr << error.what() << '\n'; return 1; }
    return 0;
}
