"""Task 6: Design Challenge – Robust Cultural Fest Registration Desk Processor."""
import os
import tempfile

def valid_email(email):
    if "@" not in email or email.count("@") != 1:
        return False
    user, domain = email.split("@")
    return bool(user) and "." in domain and not domain.startswith(".") and not domain.endswith(".")

def process_fest_files(file_paths):
    seen_regs = set()
    master = []
    by_event = {}
    errors = []
    for fp in file_paths:
        try:
            with open(fp, "r", encoding="utf-8") as f:
                for line_no, raw in enumerate(f, 1):
                    line = raw.strip()
                    if not line:
                        continue
                    parts = [p.strip() for p in line.split(",")]
                    if len(parts) != 5:
                        errors.append((fp, line_no, "Malformed column count"))
                        continue
                    reg, name, dept, email, events_str = parts
                    if reg in seen_regs:
                        errors.append((fp, line_no, f"Duplicate registration: {reg}"))
                        continue
                    if not valid_email(email):
                        errors.append((fp, line_no, f"Invalid email: {email}"))
                        continue
                    events = [e.strip() for e in events_str.split(";") if e.strip()]
                    if not events:
                        errors.append((fp, line_no, "No events selected"))
                        continue
                    seen_regs.add(reg)
                    master.append((reg, name, dept, email, events))
                    for ev in events:
                        by_event.setdefault(ev, []).append((reg, name, dept))
        except FileNotFoundError:
            errors.append((fp, 0, "Department file missing"))
    return master, by_event, errors

if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as d:
        cse = os.path.join(d, "cse.csv")
        open(cse, "w").write(
            "1911260161,Tharun,CSE,tharun@simats.edu,Hackathon;Coding\n"
            "1911260161,Tharun,CSE,tharun@simats.edu,Robotics\n"
            "1911260165,Arjun,CSE,bad-email,Coding\n"
        )
        m, evs, errs = process_fest_files([cse, os.path.join(d, "missing_ece.csv")])
        print("Master count:", len(m), "| Events:", list(evs.keys()), "| Errors:", errs)
