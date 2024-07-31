number_rows = 2
header_rows = { row: [] for row in range(number_rows)}

print(header_rows, len(header_rows.keys()))


header_rows = [[] for row in range(number_rows)]

print(header_rows, len(header_rows))