def percentage(present, total):
    return round((present / total) * 100, 2) if total else 0.0

def consecutive_absences(records, streak=3):
    by_student = {}
    for reg, _, status in records:
        by_student.setdefault(reg, []).append(status)
    flagged = []
    for reg, statuses in by_student.items():
        run = 0
        for s in statuses:
            run = run + 1 if s == "A" else 0
            if run >= streak:
                flagged.append(reg)
                break
    return flagged
