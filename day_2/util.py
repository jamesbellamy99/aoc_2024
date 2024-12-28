def parse_file(filename: str):
    reports = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            str_report = line.split()
            reports.append([int(i) for i in str_report])
    return reports


def is_report_safe(report, dampen_results=False):
    safe = False
    if dampen_results:
        if (result := is_report_safe_impl(report)) == True:
            safe = True
        else:
            # If damped_results is enabled, then test to see if a removing a single
            # index makes the result safe
            # Try removing the two indexs which caused the first attempt to fail
            # and the first two incase it's because of the starting gradient
            first_failing_index, second_failing_index = result
            indexes_to_try_removing = set(
                [first_failing_index, second_failing_index, 0, 1]
            )
            for index in indexes_to_try_removing:
                if is_report_safe_without_index(report, index):
                    safe = True
                    break
    else:
        if is_report_safe_impl(report) == True:
            safe = True

    print(f"Report: {report} is safe: {safe}")
    return safe


def is_report_safe_without_index(report, i):
    copied_report = report.copy()
    copied_report.pop(i)
    copied_result = is_report_safe_impl(copied_report)
    if copied_result == True:
        return True
    else:
        return False


def is_report_safe_impl(report):
    first_index = 0
    second_index = 1
    started_increasing = report[first_index] < report[second_index]
    while second_index < len(report):
        difference = report[first_index] - report[second_index]
        abs_dif = abs(difference)

        if abs_dif < 1:
            return first_index, second_index

        if abs_dif > 3:
            return first_index, second_index

        if started_increasing:
            if difference > 0:
                return first_index, second_index
        else:
            if difference < 0:
                return first_index, second_index
        first_index += 1
        second_index += 1
    return True
