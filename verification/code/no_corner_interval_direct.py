"""Finite Lemma 2.3: direct recursive horn DP with exact integers."""
from __future__ import annotations
from functools import lru_cache
from itertools import product
import math
def ensure(condition, message):
    if not condition: raise RuntimeError(message)

def explicit_bound(
    low: tuple[int, int, int], high: tuple[int, int, int], scale: int
) -> int:
    lower_weights = (scale, low[0], low[1])
    upper_weights = (scale, high[0], high[1])
    maximum_height = high[2]
    caps = tuple(maximum_height // weight for weight in lower_weights)
    ensure(all(0 <= cap <= 24 for cap in caps), "a coordinate cap exceeds 24")

    @lru_cache(maxsize=None)
    def horn(axis: int, level: int, first_cap: int, second_cap: int) -> int:
        if level > caps[axis]:
            return 0
        transverse = [coordinate for coordinate in range(3) if coordinate != axis]
        first_axis, second_axis = transverse
        maximum = 0
        for first in range(first_cap + 1):
            for second in range(second_cap + 1):
                if (
                    lower_weights[axis] * level
                    + lower_weights[first_axis] * first
                    + lower_weights[second_axis] * second
                    > maximum_height
                ):
                    continue
                count = (first + 1) * (second + 1)
                section_score = count * (
                    4 * upper_weights[axis] * level
                    + 2 * upper_weights[first_axis] * first
                    + 2 * upper_weights[second_axis] * second
                    - 3 * low[2]
                    + scale
                )
                maximum = max(
                    maximum,
                    section_score + horn(axis, level + 1, first, second),
                )
        return maximum

    answer: int | None = None
    for center in product(*(range(cap + 1) for cap in caps)):
        if sum(x * y for x, y in zip(center, lower_weights, strict=True)) > maximum_height:
            continue
        count = math.prod(coordinate + 1 for coordinate in center)
        score = count * (
            2 * sum(x * y for x, y in zip(center, upper_weights, strict=True))
            - 3 * low[2]
            + scale
        )
        for axis in range(3):
            transverse = [coordinate for coordinate in range(3) if coordinate != axis]
            score += horn(
                axis,
                center[axis] + 1,
                center[transverse[0]],
                center[transverse[1]],
            )
        answer = score if answer is None else max(answer, score)
    ensure(answer is not None, "central-box search is empty")
    return answer
