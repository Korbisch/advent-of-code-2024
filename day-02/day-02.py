lines = []

with open("./input.txt", 'r') as file:
    for line in file:
        line = list(map(int, line.split()))
        lines.append(line)

def calc_safe_reports() -> int:
    safe_counter = 0
    for report in lines:
        if is_safe(report): safe_counter += 1
    return safe_counter

def is_safe(report: list) -> bool:
    diffs = [report[i] - report[i+1] for i in range(len(report) - 1)]

    if all(dif in [1,2,3] for dif in diffs): return True
    if all(dif in [-1,-2,-3] for dif in diffs): return True

    return False

reports = calc_safe_reports()
print(f"Number of safe reports: {str(reports)}")


def calc_dampener_safe():
    safe_counter = 0
    for report in lines:
        if is_safe_dampened(report): safe_counter += 1
    return safe_counter

def is_safe_dampened(report: list) -> bool:
    if is_safe(report): return True
    for i in range(len(report)):
        modified = report[:i] + report[i+1:]
        if is_safe(modified): return True
    return False

reports_dampened = str(calc_dampener_safe())
print(f"Number of safe dampened reports: {reports_dampened}")
