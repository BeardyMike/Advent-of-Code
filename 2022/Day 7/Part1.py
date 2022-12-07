import itertools
def partone(s, bool):
    part2=bool
    dir, sizes = [], []
    for line in s.splitlines():
        if line == '$ cd ..':
            size = dir.pop()
            sizes.append(size)
            dir[-1] += size
        elif line.startswith('$ cd '):
            dir.append(0)
        elif line[0].isdigit():
            dir[-1] += int(line.split()[0])
    sizes.extend(itertools.accumulate(dir[::-1]))
    if part2:
        return min(s for s in sizes if s >= max(sizes) - 40000000)
    else:
        return sum(s for s in sizes if s <= 100000)

"""
1. Split the input string into lines.
2. If the line is $ cd .., pop the last element from the dir list and add it to the second-to-last element. Then add the size to the sizes list.
3. If the line starts with $ cd, append 0 to the dir list.
4. If the line starts with a digit, add the size to the last element in the dir list.
5. Extend the sizes list with the cumulative sum of the dir list, reversed.
6. If part2 is True, return the minimum size in the sizes list that is greater than or equal to the maximum size in the sizes list minus 40,000,000.
7. Otherwise, return the sum of the sizes in the sizes list that are less than or equal to 100,000. 
"""