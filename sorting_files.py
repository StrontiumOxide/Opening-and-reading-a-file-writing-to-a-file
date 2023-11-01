list_info = []
for order in range(1,4):
    with open(file=f"file_{order}.txt", mode="r", encoding="utf-8") as f:
        info = f.readlines()
        list_info.append((f"file_{order}.txt\n{len(info)}\n{''.join(info)}", len(info)))

for info in sorted(list_info, key=lambda x: x[1]):
    with open(file="file_end.txt", mode="a", encoding="utf-8") as f:
        f.write(f"{info[0]}\n\n")
