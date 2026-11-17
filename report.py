def format_report(flagged):
    return "3-Day Consecutive Absentees: " + (", ".join(flagged) if flagged else "None")
