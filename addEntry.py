import re
import bisect


def problemNameToFileName(s: str):
    return "".join(filter(lambda c: c.isalnum(), s))


def problemNameToURL(s: str) -> str:
    s = re.sub(r"-", " ", s.lower())
    s = re.sub(r"[^\w ]", "", s)
    s = re.sub(r"\s+", "-", s)
    return f"https://leetcode.com/problems/{s}/description/"


def fileExtensionToName(ext):
    match ext:
        case 'cpp':
            return 'C++'
        case 'c':
            return 'C'
        case 'py':
            return 'Python'
        case 'js':
            return 'JavaScript'
        case 'sql':
            return 'SQL'
        case _:
            raise Exception('Unknown file extension')


def getDifficultyString(diff: str) -> str:
    if diff.lower() in {"easy", "medium", "hard"}:
        return diff.capitalize()

    match diff.lower():
        case "e":
            return "Easy"
        case "m":
            return "Medium"
        case "h":
            return "Hard"
        case _:
            raise Exception("Invalid difficulty")


def addEntry(num, name, diff, ext):
    FILE_NAME = 'README.md'
    # 0-based index
    ENTRIES_BEGIN = 6

    with open(f'./{FILE_NAME}', 'r') as f:
        lines = [line for line in f]

    with open(f'./{FILE_NAME}', 'w') as f:
        def getEntryID(line: str) -> int:
            return int(re.search('(?<=(\| ))\d{1,4}', line).group(0))

        try:
            insertIdx = bisect.bisect_left(lines,
                                           num,
                                           key=getEntryID,
                                           lo=ENTRIES_BEGIN)

            # assumption: file is properly formatted
            newline = f'| {num} | [{name}]({problemNameToURL(name)}) | [{fileExtensionToName(ext)}](https://github.com/jinxuan-owyong/leetcode/blob/master/{ext}/{num:04}_{problemNameToFileName(name)}.{ext}) | {diff} |\n'
            lines.insert(insertIdx, newline)

        finally:
            problemFileName = f'{num:04}_{problemNameToFileName(name)}.{ext}'
            f.write(''.join(lines))

    match ext:
        case "py":
            # copy template file
            with open("py/template.py") as f:
                lines = f.readlines()
                with open(f'{ext}/{problemFileName}', 'w+') as f1:
                    f1.write(f'# {num}. {name}\n')
                    f1.writelines(lines)
        case "js":
            with open(f'{ext}/{problemFileName}', 'w+') as f1:
                f1.write(f'// {num}. {name}\n')
        case "sql":
            with open(f'{ext}/{problemFileName}', 'w+') as f1:
                f1.write(f'-- {num}. {name}\n')


if __name__ == "__main__":
    problem = input('Problem: ').strip()
    num, name = problem.split('. ')
    diff = input('Difficulty: ').strip()
    ext = input('File extension: ').strip().lower()
    addEntry(int(num), name, getDifficultyString(diff), ext)
