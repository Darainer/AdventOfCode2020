
from io import TextIOWrapper


def Customs_checker(text: TextIOWrapper) -> bool:
    count = 0
    group = set()
    for line in text:
        if line != '\n':
            raw_line = line.strip('\n')
            for string in raw_line:
                group.add(string)
        else:
            count += len(group)
            group.clear()
    count += len(group)
    return count


def Count_group_common_answers(text: TextIOWrapper) -> bool:
    count = 0
    group = list()
    for line in text:
        if line != '\n':
            group.append(set())
            raw_line = line.strip('\n')
            for string in raw_line:
                group[-1].add(string)
        else:
            count += len(group.pop().intersection(*group))
            group.clear()
    return count
