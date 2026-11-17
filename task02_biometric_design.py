"""Task 2: Biometric Attendance Multi-File Streaming Processor."""
from pathlib import Path
import tempfile

def process_attendance_folder(folder_path):
    counts = {}  # reg_no -> [present, total]
    damaged = []
    for file_path in sorted(Path(folder_path).glob("*.csv")):
        with file_path.open("r", encoding="utf-8") as f:
            for line_no, raw in enumerate(f, 1):
                line = raw.strip()
                if not line:
                    continue
                parts = [p.strip() for p in line.split(",")]
                if len(parts) != 3 or parts[2] not in ("P", "A"):
                    damaged.append((file_path.name, line_no, line))
                    continue
                reg, _, status = parts
                rec = counts.setdefault(reg, [0, 0])
                rec[1] += 1
                if status == "P":
                    rec[0] += 1
    summary = {r: round((p / t) * 100, 2) for r, (p, t) in counts.items()}
    low_att = [r for r, pct in summary.items() if pct < 75.0]
    return summary, low_att, damaged

if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as d:
        Path(d, "day1.csv").write_text("1911260161,2026-10-01,P\n1911260162,2026-10-01,A\nBAD_LINE\n", encoding="utf-8")
        Path(d, "day2.csv").write_text("1911260161,2026-10-02,P\n1911260162,2026-10-02,A\n", encoding="utf-8")
        s, low, dmg = process_attendance_folder(d)
        print("Summary:", s, "| Below 75%:", low, "| Damaged:", dmg)
