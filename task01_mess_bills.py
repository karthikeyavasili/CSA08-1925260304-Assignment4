"""Task 1: Streaming Hostel Mess Bill Processor with Specific Exceptions."""
from decimal import Decimal, InvalidOperation
import tempfile
import os

def process_mess_bills(filepath):
    total = Decimal("0.00")
    report_lines = []
    rejected = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line_no, raw in enumerate(f, 1):
                line = raw.strip()
                if not line:
                    continue
                parts = [p.strip() for p in line.split(",")]
                if len(parts) != 3:
                    rejected.append((line_no, line, "Expected 3 fields"))
                    continue
                reg_no, name, amt_str = parts
                try:
                    amt = Decimal(amt_str)
                    if amt < 0:
                        raise ValueError("Negative amount")
                except (InvalidOperation, ValueError) as exc:
                    rejected.append((line_no, line, str(exc)))
                    continue
                total += amt
                report_lines.append(f"{reg_no:<12} {name:<20} Rs {amt:8.2f}")
    except FileNotFoundError:
        return "", Decimal("0.00"), [(0, filepath, "File not found")]
    return "\n".join(report_lines), total, rejected

if __name__ == "__main__":
    sample = "1911260161,Tharun,1250.50\n1911260162,Ravi,bad_amt\n\n1911260163,Anu,980.00\n"
    with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as tmp:
        tmp.write(sample)
        path = tmp.name
    rep, tot, rej = process_mess_bills(path)
    os.remove(path)
    print(rep)
    print("Total:", tot, "| Rejected:", rej)
