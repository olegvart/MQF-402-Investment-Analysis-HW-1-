from pathlib import Path

file_path = Path("data/Portfolios_Formed_on_Size_daily.txt")

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

header = ['date']+lines[0].strip().split()

data = []

for line in lines[1:]:
    values = line.strip().split()

    if len(values) == 16:
        date = values[0]
        year = int(values[1])
        month = int(values[2])
        day = int(values[3])
        returns = [float(value) for value in values[4:]]

        row = {
            "date": date,
            "year": year,
            "month": month,
            "day": day,
            "returns": returns
        }

        data.append(row)

print(data)