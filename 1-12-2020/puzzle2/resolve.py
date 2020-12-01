import pandas as pd 

expense_report = pd.read_csv("input", 'r', header=None)
expense_report.columns = ["expense"]
print(expense_report)


for i in range(len(expense_report)):
    for j in range(i+1, len(expense_report)):
        for k in range(j+1, len(expense_report)):
            if expense_report.iloc[i, 0] + expense_report.iloc[j, 0] + expense_report.iloc[k,0] == 2020:
                answer = expense_report.iloc[i, 0] * expense_report.iloc[j, 0] * expense_report.iloc[k,0]
                print(expense_report.iloc[i, 0], expense_report.iloc[j, 0], expense_report.iloc[k,0])
                break


print(answer)
