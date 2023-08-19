import re


def arithmetic_arranger(problems, solve=False):
  if (len(problems) > 5):
    return "Error: Too many problems."

  top = ""
  bottom = ""
  dashes = ""
  solution = ""
  arranged_problems = ""

  for problem in problems:
    if (re.search("[^\s0-9+-]", problem)):
      if (re.search("[/]", problem) or re.search("[*]", problem)):
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."

    firstOperand = problem.split()[0]
    operator = problem.split()[1]
    secondOperand = problem.split()[2]

    if (len(firstOperand) > 4 or len(secondOperand) > 4):
      return "Error: Numbers cannot be more than four digits."

    answer = ""
    if (operator == "+"):
      answer = str(sum([int(firstOperand), int(secondOperand)]))
    else:
      answer = str(sum([int(firstOperand), -int(secondOperand)]))

    length = max(len(firstOperand), len(secondOperand)) + 2

    dash = ""
    for i in range(length):
      dash += "-"

    if problem != problems[-1]:
      top += firstOperand.rjust(length) + "    "
      bottom += operator + secondOperand.rjust(length - 1) + "    "
      dashes += dash + "    "
      solution += answer.rjust(length) + "    "
    else:
      top += firstOperand.rjust(length)
      bottom += operator + secondOperand.rjust(length - 1)
      dashes += dash
      solution += answer.rjust(length)

    if solve:
      arranged_problems = top + "\n" + bottom + "\n" + dashes + "\n" + solution
    else:
      arranged_problems = top + "\n" + bottom + "\n" + dashes

  return arranged_problems
