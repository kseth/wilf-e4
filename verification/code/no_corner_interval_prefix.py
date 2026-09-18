"""Finite Lemma 2.3: prefix-maxima horn DP with exact integers."""
from __future__ import annotations
def require(condition, message):
    if not condition: raise RuntimeError(message)

def prefix_bound(
    lower: tuple[int, int, int], upper: tuple[int, int, int], scale: int
) -> int:
    feasible = (scale, lower[0], lower[1])
    objective = (scale, upper[0], upper[1])
    height = upper[2]
    offset = scale - 3 * lower[2]
    caps = tuple(height // weight for weight in feasible)
    require(all(0 <= cap <= 24 for cap in caps), "coordinate cap is outside the proved range")

    horns: list[tuple[list[list[int]], int]] = []
    for axis in range(3):
        other = tuple(index for index in range(3) if index != axis)
        rows = caps[other[0]] + 1
        columns = caps[other[1]] + 1
        layers = [[0] * (rows * columns) for _ in range(caps[axis] + 2)]
        for level in range(caps[axis], -1, -1):
            current = layers[level]
            tail = layers[level + 1]
            for first in range(rows):
                row_maximum = 0
                for second in range(columns):
                    index = first * columns + second
                    if (
                        feasible[axis] * level
                        + feasible[other[0]] * first
                        + feasible[other[1]] * second
                        <= height
                    ):
                        count = (first + 1) * (second + 1)
                        section = count * (
                            offset
                            + 4 * objective[axis] * level
                            + 2 * objective[other[0]] * first
                            + 2 * objective[other[1]] * second
                        )
                        row_maximum = max(row_maximum, section + tail[index])
                    prior_row = current[index - columns] if first else 0
                    current[index] = max(row_maximum, prior_row)
        horns.append((layers, columns))

    result: int | None = None
    for x in range(caps[0] + 1):
        for y in range(caps[1] + 1):
            for z in range(caps[2] + 1):
                center = (x, y, z)
                if sum(a * b for a, b in zip(feasible, center, strict=True)) > height:
                    continue
                count = (x + 1) * (y + 1) * (z + 1)
                score = count * (
                    offset
                    + 2 * sum(a * b for a, b in zip(objective, center, strict=True))
                )
                for axis in range(3):
                    other = tuple(index for index in range(3) if index != axis)
                    layers, columns = horns[axis]
                    score += layers[center[axis] + 1][
                        center[other[0]] * columns + center[other[1]]
                    ]
                result = score if result is None else max(result, score)
    require(result is not None, "no feasible central box")
    return result
