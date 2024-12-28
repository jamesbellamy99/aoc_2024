def parse_file(filename: str):
    reports = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            str_report = line.split()
            reports.append([int(i) for i in str_report])
    return reports

def is_report_safe(report, dampen_results=False):
    if dampen_results:
        result = is_report_safe_impl(report)
        if result == True:
            return True
        else:
            # This could definaitly be improved, as we're brute force dampening rather
            # than focusing on the failing levels 
            for i in range(0, len(report)):
                copied_report = report.copy()
                copied_report.pop(i)
                copied_result = is_report_safe_impl(copied_report)
                if copied_result == True:
                    return True
            return False
    else:
        result = is_report_safe_impl(report)
        if result == True:
            return True
        else:
            return False


def is_report_safe_impl(report):
    print(f"Checking {report}")
    first_index = 0
    second_index = 1
    started_increasing = report[first_index] < report[second_index]
    while second_index < len(report):
        difference  = report[first_index] - report[second_index]
        abs_dif = abs(difference)

        if abs_dif < 1:
            print(f"Report is changing by less than 1 because of {report[first_index]} and {report[second_index]}")
            return first_index, second_index
        
        if abs_dif > 3:
            print(f"Report is changing by more than 3 because of {report[first_index]} and {report[second_index]}")
            return first_index, second_index
        
        if started_increasing:
            if difference > 0:
                print(f"Report is no longer increasing because of {report[first_index]} and {report[second_index]}")
                return first_index, second_index
        else:
            if difference < 0:
                print(f"Report is no longer decreasing because of {report[first_index]} and {report[second_index]}")
                return first_index, second_index
        first_index += 1
        second_index += 1
    print("Report is safe")
    return True