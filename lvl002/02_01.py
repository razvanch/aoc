# http://adventofcode.com/2017/day/2

with open("02_01.in") as f:
    spreadsheet = []

    for line in f:
        text = line.strip()

        if not text:
            break

        spreadsheet_line = [int(number) for number in text.split(" ")
                            if number]

        spreadsheet.append(spreadsheet_line)

checksum = 0

# your code goes in here

print(checksum)
