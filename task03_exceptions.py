"""Task 3: Custom Exceptions and Complete try/except/else/finally Handling."""
import os
import tempfile

class InvalidRecord(Exception):
    """Raised when a line of the attendance file is not in the expected format."""

def parse_line(line):
    """'192311001,2026-10-08,P' -> ('192311001', '2026-10-08', 'P')"""
    parts = line.strip().split(",")
    # TODO 1 Completed
    if len(parts) != 3:
        raise InvalidRecord(f"expected 3 fields, found {len(parts)}")
    if parts[2] not in ("P", "A"):
        raise InvalidRecord(f"invalid status '{parts[2]}'")
    return (parts[0], parts[1], parts[2])

def summarise(path):
    present, absent, errors = 0, 0, []
    # TODO 2 Completed
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line_no, raw in enumerate(f, 1):
                if not raw.strip():
                    continue
                try:
                    _, _, status = parse_line(raw)
                except InvalidRecord as exc:
                    errors.append((line_no, str(exc)))
                else:
                    if status == "P":
                        present += 1
                    else:
                        absent += 1
    except FileNotFoundError as exc:
        errors.append((0, f"File missing: {exc.filename}"))
    finally:
        pass
    return present, absent, errors

if __name__ == "__main__":
    data = ("192311001,2026-10-08,P\n192311002,2026-10-08,A\n"
            "192311003,2026-10-08\n192311004,2026-10-08,L\n")
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8") as tmp:
        tmp.write(data)
        name = tmp.name
    print(summarise(name))
    os.remove(name)
    print("Missing file check:", summarise("non_existent_file.csv"))
