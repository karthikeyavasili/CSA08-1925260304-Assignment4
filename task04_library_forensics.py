"""Task 4: File and Exception Forensics – Repaired Library Returns Logger."""
import tempfile
import os

def save_returns_fixed(books, log_path="returns.log"):
    with open(log_path, "a", encoding="utf-8") as log:
        for b in books:
            clean = b.strip()
            if clean:
                log.write(clean + "\n")

def process_fixed(day_file, log_path="returns.log", err_path="errors.log"):
    try:
        with open(day_file, "r", encoding="utf-8") as f:
            books = f.readlines()
        save_returns_fixed(books, log_path)
    except OSError as exc:
        with open(err_path, "a", encoding="utf-8") as err:
            err.write(f"[ERROR] {day_file}: {exc}\n")

if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as d:
        d1 = os.path.join(d, "day1.txt")
        d2 = os.path.join(d, "day2.txt")
        log_f = os.path.join(d, "returns.log")
        err_f = os.path.join(d, "errors.log")
        open(d1, "w").write("Clean Code\nPython Crash Course\n")
        open(d2, "w").write("Fluent Python\n")
        process_fixed(d1, log_f, err_f)
        process_fixed(d2, log_f, err_f)
        process_fixed("missing_day3.txt", log_f, err_f)
        print("Returns Log:\n" + open(log_f).read().strip())
        print("Error Log:\n" + open(err_f).read().strip())
