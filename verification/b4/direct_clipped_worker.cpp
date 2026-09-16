// Independent R4a backend: disjoint clipped boxes and DIRECT transitions.
// No prefix-maximum recurrence or upper-box subtraction is used.
#include <algorithm>
#include <array>
#include <iostream>
#include <limits>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

using Integer = long long;
using Triple = std::array<Integer, 3>;
static_assert(std::numeric_limits<Integer>::digits >= 63, "64-bit integers required");
static_assert(std::numeric_limits<int>::digits >= 31, "32-bit indices required");

struct Statistics {
    Integer count = 0, twice_moment = 0, maximum = 0;
};

// Partition by the FIRST coordinate below p: earlier coordinates are >= p.
Statistics measure(const Triple& a, const Triple& b, const Triple& p,
                   const Triple& feasible, const Triple& objective) {
    Statistics total;
    for (int first_below = 0; first_below < 3; ++first_below) {
        Triple lower = a, upper = b;
        for (int i = 0; i < first_below; ++i)
            lower[i] = std::max(lower[i], p[i]);
        upper[first_below] = std::min(upper[first_below], p[first_below] - 1);
        Integer volume = 1, twice_mean = 0, height = 0;
        bool empty = false;
        for (int i = 0; i < 3; ++i) {
            if (lower[i] > upper[i]) { empty = true; break; }
            volume *= upper[i] - lower[i] + 1;
            twice_mean += objective[i] * (lower[i] + upper[i]);
            height += feasible[i] * upper[i];
        }
        if (!empty) {
            total.count += volume;
            total.twice_moment += volume * twice_mean;
            total.maximum = std::max(total.maximum, height);
        }
    }
    return total;
}

Integer solve(Integer scale, const Triple& lower, const Triple& upper,
              const Triple& p) {
    const Triple feasible{scale, lower[0], lower[1]};
    const Triple objective{scale, upper[0], upper[1]};
    const Integer constant = scale - 3 * lower[2];
    std::array<int, 3> sizes;
    for (int i = 0; i < 3; ++i)
        sizes[i] = static_cast<int>(upper[2] / feasible[i]) + 1;
    std::array<std::vector<std::vector<Integer>>, 3> horns;
    for (int axis = 0; axis < 3; ++axis) {
        const int j = axis == 0 ? 1 : 0;
        const int k = axis == 2 ? 1 : 2;
        const int rows = sizes[j], columns = sizes[k];
        horns[axis].assign(sizes[axis] + 1,
                           std::vector<Integer>(rows * columns, 0));
        for (int level = sizes[axis] - 1; level >= 0; --level) {
            const auto& tail = horns[axis][level + 1];
            auto& here = horns[axis][level];
            std::vector<Integer> candidates(rows * columns, 0);
            for (int r = 0; r < rows; ++r) for (int s = 0; s < columns; ++s) {
                Triple a{0, 0, 0}, b{0, 0, 0};
                a[axis] = b[axis] = level;
                b[j] = r; b[k] = s;
                const auto piece = measure(a, b, p, feasible, objective);
                if (piece.maximum <= upper[2])
                    candidates[r * columns + s] =
                        2 * piece.twice_moment + constant * piece.count
                        + tail[r * columns + s];
            }
            // Enumerate EVERY permitted rectangle at EVERY state.
            for (int R = 0; R < rows; ++R) for (int S = 0; S < columns; ++S) {
                Integer best = 0; // terminate the horn
                for (int r = 0; r <= R; ++r)
                    for (int s = 0; s <= S; ++s)
                        best = std::max(best, candidates[r * columns + s]);
                here[R * columns + S] = best;
            }
        }
    }
    bool found = false;
    Integer result = 0;
    for (int x = 0; x < sizes[0]; ++x)
        for (int y = 0; y < sizes[1]; ++y)
            for (int z = 0; z < sizes[2]; ++z) {
                const Triple c{x, y, z};
                const auto central = measure({0, 0, 0}, c, p, feasible, objective);
                if (central.maximum > upper[2]) continue;
                Integer score = 2 * central.twice_moment + constant * central.count;
                for (int axis = 0; axis < 3; ++axis) {
                    const int j = axis == 0 ? 1 : 0, k = axis == 2 ? 1 : 2;
                    score += horns[axis][c[axis] + 1][c[j] * sizes[k] + c[k]];
                }
                if (!found || score > result) result = score;
                found = true;
            }
    if (!found) throw std::runtime_error("no feasible central box");
    return result;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    try {
        std::string line;
        while (std::getline(std::cin, line)) {
            std::istringstream input(line);
            Integer scale; Triple lower, upper;
            std::string extra;
            if (!(input >> scale >> lower[0] >> lower[1] >> lower[2]
                        >> upper[0] >> upper[1] >> upper[2]) || (input >> extra))
                throw std::runtime_error("malformed request");
            if (scale != 4096 || lower[2] < 6 * scale)
                throw std::runtime_error("unsupported scale or height");
            for (int i = 0; i < 3; ++i)
                if (lower[i] < scale || lower[i] > upper[i] || upper[i] > 42 * scale)
                    throw std::runtime_error("request outside proved root bounds");
            bool first = true;
            for (const Triple p : {Triple{2, 1, 1}, Triple{1, 2, 1}, Triple{1, 1, 2}}) {
                if (!first) std::cout << ' ';
                std::cout << solve(scale, lower, upper, p);
                first = false;
            }
            std::cout << '\n';
        }
        if (!std::cin.eof()) throw std::runtime_error("input read failure");
    } catch (const std::exception& error) {
        std::cerr << error.what() << '\n';
        return 1;
    }
    return 0;
}
