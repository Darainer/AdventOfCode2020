
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

    return count
