from typing import Dict, List
from prettytable import PrettyTable
import argparse


def open_csv_file(file_path: str = None) -> List:
    """
    Open csv file from given path.
    Args: file_path - path to csv file
    Return: list of lines with report info without header
    """
    with open(file_path, "r") as f:
        report_per_line = f.readlines()
        f.close()
    return report_per_line[1:]


def apply_menu_task_1(report_per_line: List, to_print: bool = True) -> None:
    """
    Collect hierarchy of the teams inside the departments.
    Print it if to_print is True.
    Args:
        report_per_line - list of lines with report info without header,
        to_print - beautiful table print with info
    Return: None
    """
    departments_info = {}
    for line in report_per_line:
        current_info = line.split(";")
        currrent_department_name = current_info[1]
        current_team = current_info[2]
        if currrent_department_name not in departments_info.keys():
            departments_info[currrent_department_name] = set([current_team])
        elif current_team not in departments_info[currrent_department_name]:
            departments_info[currrent_department_name].add(current_team)

    # Beautiful output
    if to_print:
        output = PrettyTable()
        output.field_names = ["Department name", "Teams inside department"]
        for name, teams_names in departments_info.items():
            output.add_row([name, ", ".join(teams_names)])
        print(output)


def apply_menu_task_2(report_per_line: List, to_print: bool = True) -> Dict:
    """
    Collect info about every department salary and employee amount.
    Print it if to_print is True.
    Args:
        report_per_line - list of lines with report info without header,
        to_print - beautiful table print with info
    Return: dict with summary for every department inside report_per_line
    """
    departments_info = {}
    for line in report_per_line:
        current_info = line.replace("\n", "").split(";")
        currrent_department_name = current_info[1]
        currrent_department_salary = int(current_info[5])
        if departments_info.get(currrent_department_name):
            departments_info[currrent_department_name].append(
                currrent_department_salary
            )
        else:
            departments_info[currrent_department_name] = [currrent_department_salary]

    departments_summary = {}
    for name, salaries in departments_info.items():
        departments_summary[name] = {
            "count": len(salaries),
            "min_salary": min(salaries),
            "max_salary": max(salaries),
            "mean_salary": round(sum(salaries) / len(salaries), 1),
        }

    # Beautiful output
    if to_print:
        output = PrettyTable()
        output.field_names = [
            "Department name",
            "Employee count",
            "Min salary",
            "Max salary",
            "Mean salary",
        ]
        for name, salary_info in departments_summary.items():
            output.add_row([name] + list(salary_info.values()))
        print(output)
    return departments_summary


def apply_menu_task_3(
    departments_summary: Dict, output_name: str = "summary_report.csv"
) -> None:
    """
    Save dict with summary for every department inside report_per_line into csv file
    to current dicrectory.
    Args:
        departments_summary - dict with summary info per department,
        output_name - name for the output csv file
    Return: None
    """
    with open(output_name, "w+") as f:
        f.write(
            ";".join(
                [
                    "Department name",
                    "Employee count",
                    "Min salary",
                    "Max salary",
                    "Mean salary",
                ]
            )
            + "\n"
        )
        for name, salary_info in departments_summary.items():
            f.write(
                ";".join([name] + [str(num) for num in salary_info.values()]) + "\n"
            )
    print(f"Report is saved to {output_name}")


def main():
    # Add and parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--csv_path",
        type=str,
        default="./Corp_Summary.csv",
        help="path of the csv file",
    )
    args = parser.parse_args()

    # Open and read csv file
    report = open_csv_file(args.csv_path)
    salary_summary = None
    option = None
    options = set(["1", "2", "3", "menu", "quit"])
    menu_info = (
        "Выберите пункт меню из списка ниже:\n"
        "1 - Вывести в понятном виде иерархию команд,"
        "т.e. департамент и все команды, которые входят в него.\n"
        "2 - Вывести сводный отчёт по департаментам: название, численность,"
        "'вилка' зарплат в виде мин - макс, среднюю зарплату.\n"
        "3 - Сохранить сводный отчёт из предыдущего пункта в виде csv-файла."
        "При этом необязательно вызывать сначала команду из п.2.\n"
        "menu - Отобразить пункты еще раз.\n"
        "quit - Выйти из программы."
    )
    print(menu_info)
    while option != "quit":
        print("Ваш выбор:", end="")
        option = input()
        if option not in options:
            print(
                "Введите корректный пункт из меню,",
                " menu для отображения списка,",
                " либо quit для выхода.",
            )
        if option == "1":
            apply_menu_task_1(report)
        elif option == "2":
            salary_summary = apply_menu_task_2(report)
        elif option == "3":
            if salary_summary is None:
                salary_summary = apply_menu_task_2(report, to_print=False)
            apply_menu_task_3(salary_summary)
        elif option == "menu":
            print(menu_info)


if __name__ == "__main__":
    main()
