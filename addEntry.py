import re
import bisect
from typing import List
import os


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
        case 'go':
            return 'Go'
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


def addEntry(num, name, diff, ext, createTemplate=True):
    fileType = fileExtensionToName(ext)
    FILE_NAME = f'{ext}/README.md'
    # 0-based index
    ENTRIES_BEGIN = 4

    with open(f'./{FILE_NAME}', 'r') as f:
        lines = [line for line in f]

    with open(f'./{FILE_NAME}', 'w') as f:
        def getEntryID(line: str) -> int:
            return int(re.search(r'(?<=(\| ))\d{1,4}', line).group(0))

        try:
            insertIdx = bisect.bisect_left(lines,
                                           num,
                                           key=getEntryID,
                                           lo=ENTRIES_BEGIN)

            # assumption: file is properly formatted
            problemFileName = f'{num:04}_{problemNameToFileName(name)}.{ext}'
            if ext == 'go':
                pathToFile = f'{ext}/{num:04}/{problemFileName}'
            else:
                pathToFile = f'{ext}/{problemFileName}'

            githubFileUrl = f'https://github.com/jinxuan-owyong/leetcode/blob/master/{
                pathToFile}'

            newline = f'| {num} | [{name}]({problemNameToURL(name)}) | [{
                problemFileName}]({githubFileUrl}) | {diff} |\n'
            lines.insert(insertIdx, newline)

        finally:
            f.write(''.join(lines))

    if createTemplate:
        commentDelimiter = {"py": "#",
                            "js": "//",
                            "sql": "--",
                            "go": "//"}

        comment = f'{commentDelimiter[ext]} {num}. {name}'
        lines = []

        # copy template file
        if ext in ("py", "js", "go"):
            with open(f"{ext}/template.{ext}") as f:
                lines = f.readlines()

        fileDir = pathToFile[:pathToFile.rfind('/')]
        if not os.path.exists(fileDir):
            os.mkdir(fileDir)

        with open(pathToFile, 'w+') as f1:
            f1.write(f'{comment}\n\n')
            if lines:
                f1.writelines(lines)


if __name__ == "__main__":
    problem = input('Problem: ').strip()
    num, name = problem.split('. ')
    diff = input('Difficulty: ').strip()
    ext = input('File extension: ').strip().lower()
    addEntry(int(num), name, getDifficultyString(diff), ext)
