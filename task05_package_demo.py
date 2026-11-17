"""Task 5: Package Organisation Demonstration."""
from attendance import read_records, consecutive_absences, format_report

if __name__ == "__main__":
    raw = [
        "1911260161,2026-10-01,A",
        "1911260161,2026-10-02,A",
        "1911260161,2026-10-03,A",
        "1911260162,2026-10-01,P",
    ]
    recs = read_records(raw)
    print(format_report(consecutive_absences(recs)))
