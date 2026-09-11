#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <vector>

// Exact exhaustive Wilf-4 check for the p211 congruence union in the generator box
// m < a < b < c <= m*(m-2). No external libraries or floating-point tests.
// The conductor-reduction theorem in the accompanying note proves that
// every negative Wilf-4 semigroup at multiplicity m is inside this box.
constexpr int INF = 1000000000;

// Adjoin a generator w to a residue shortest-path vector. Translation by
// w mod m consists of gcd(m,w) disjoint directed cycles. Two complete
// forward passes propagate every possible source around each entire cycle.
static void adjoin(const std::vector<int>& before, int w,
                   std::vector<int>& after) {
    const int m = static_cast<int>(before.size());
    after = before;
    const int step = w % m;
    const int g = std::gcd(m, step);
    const int length = m / g;
    for (int start = 0; start < g; ++start) {
        int r = start;
        for (int k = 0; k < 2 * length; ++k) {
            int next = r + step;
            if (next >= m) next -= m;
            after[next] = std::min(after[next], after[r] + w);
            r = next;
        }
    }
}

struct Stats {
    std::uint64_t raw = 0, small_redundant = 0, middle_redundant = 0;
    std::uint64_t largest_redundant = 0, gcd_bad = 0, valid = 0;
    std::uint64_t bounded = 0, negative = 0, zero = 0;
    std::uint64_t checksum = 14695981039346656037ULL;
    long long min_w = (1LL << 60), min_bounded_w = (1LL << 60);
    std::array<int, 4> minimizer{}, bounded_minimizer{};
};

static void mix(Stats& s, std::uint64_t value) {
    // FNV-1a on the eight little-endian bytes of each integer, to provide
    // a reproducible traversal check (not a substitute for the proof).
    for (int k = 0; k < 8; ++k) {
        s.checksum ^= value & 255;
        s.checksum *= 1099511628211ULL;
        value >>= 8;
    }
}

static void emit_array(const std::array<int, 4>& a) {
    std::cout << '[' << a[0] << ',' << a[1] << ',' << a[2] << ',' << a[3] << ']';
}

static void run(int m) {
    auto start = std::chrono::steady_clock::now();
    const int bound = m * (m - 2);
    const std::uint64_t n = bound - m;
    Stats s;
    (void)n; // raw count is accumulated over the exact congruence union.
    std::vector<int> origin(m, INF), da(m), dab(m), dabc(m);
    origin[0] = 0;
    for (int a = m + 1; a <= bound - 2; ++a) {
        const bool bad_a = a % m == 0;
        if (!bad_a) adjoin(origin, a, da);
        for (int b = a + 1; b <= bound - 1; ++b) {
            // Solve c=-2a-b, c=-a-2b, or 2c=-a-b mod m.
            // The third congruence has gcd(2,m) solutions or none.
            auto residue = [m](long long x) { return int((x % m + m) % m); };
            std::vector<int> residues{residue(-2LL*a-b),residue(-a-2LL*b)};
            int rhs=residue(-a-b), h=std::gcd(2,m);
            if(rhs%h==0) {
                if(h==2) {residues.push_back(rhs/2);residues.push_back(rhs/2+m/2);}
                else residues.push_back(int((1LL*rhs*((m+1)/2))%m));
            }
            std::sort(residues.begin(),residues.end());
            residues.erase(std::unique(residues.begin(),residues.end()),residues.end());
            std::uint64_t allowed=0;
            for(int r:residues) allowed+=(bound-r)/m-(b-r)/m;
            s.raw+=allowed;
            if(bad_a) {s.small_redundant+=allowed;continue;}
            if(da[b%m]<=b) {s.middle_redundant+=allowed;continue;}
            adjoin(da,b,dab);
            const int base_gcd=std::gcd(std::gcd(m,a),b);
            for(int q=b/m;q<=bound/m;++q) for(int r:residues) {
                const int c=q*m+r;
                if(c<=b||c>bound)continue;
                if (dab[c % m] <= c) {
                    ++s.largest_redundant;
                    continue;
                }
                if (std::gcd(base_gcd, c) != 1) {
                    ++s.gcd_bad;
                    continue;
                }
                ++s.valid;
                adjoin(dab, c, dabc);
                long long sum = 0;
                int maximum = 0;
                for (int value : dabc) {
                    if (value >= INF) throw std::runtime_error("unreachable residue");
                    sum += value;
                    maximum = std::max(maximum, value);
                }
                const long long numerator = 3LL * m * maximum - 4 * sum
                                          - 1LL * m * (m - 1);
                if (numerator % m) throw std::runtime_error("nonintegral Wilf number");
                const long long wilf = numerator / m;
                if (wilf < s.min_w) {
                    s.min_w = wilf;
                    s.minimizer = {m, a, b, c};
                }
                if (wilf < 0) ++s.negative;
                if (wilf == 0) ++s.zero;
                if (maximum <= bound) {
                    ++s.bounded;
                    if (wilf < s.min_bounded_w) {
                        s.min_bounded_w = wilf;
                        s.bounded_minimizer = {m, a, b, c};
                    }
                    mix(s, a); mix(s, b); mix(s, c);
                    mix(s, maximum); mix(s, sum); mix(s, static_cast<std::uint64_t>(wilf));
                }
            }
        }
    }
    if (s.raw != s.small_redundant + s.middle_redundant + s.largest_redundant
               + s.gcd_bad + s.valid) throw std::runtime_error("count partition mismatch");
    const double elapsed = std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
    std::cout << "{\"m\":" << m << ",\"generator_bound_inclusive\":" << bound
              << ",\"raw_relation_triples\":" << s.raw
              << ",\"smallest_redundant\":" << s.small_redundant
              << ",\"middle_redundant\":" << s.middle_redundant
              << ",\"largest_redundant\":" << s.largest_redundant
              << ",\"nontrivial_gcd\":" << s.gcd_bad
              << ",\"minimal_four_generator_semigroups\":" << s.valid
              << ",\"maximum_apery_within_bound\":" << s.bounded
              << ",\"negative_wilf_count\":" << s.negative
              << ",\"zero_wilf_count\":" << s.zero
              << ",\"minimum_wilf\":" << s.min_w << ",\"minimum_wilf_example\":";
    emit_array(s.minimizer);
    std::cout << ",\"minimum_wilf_with_bounded_apery\":" << s.min_bounded_w
              << ",\"bounded_minimum_example\":";
    emit_array(s.bounded_minimizer);
    std::cout << ",\"bounded_checksum_fnv1a64\":\"" << s.checksum
              << "\",\"elapsed_seconds\":" << elapsed << "}" << std::endl;
}

int main(int argc, char** argv) {
    int lo = 30, hi = 48;
    if (argc > 1) lo = std::atoi(argv[1]);
    if (argc > 2) hi = std::atoi(argv[2]);
    if (lo < 4 || hi < lo || hi > 100) return 2;
    for (int m = lo; m <= hi; ++m) run(m);
    return 0;
}
