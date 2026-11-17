def read_records(lines):
    valid = []
    for line in lines:
        parts = [p.strip() for p in line.strip().split(",")]
        if len(parts) == 3 and parts[2] in ("P", "A"):
            valid.append(tuple(parts))
    return valid
