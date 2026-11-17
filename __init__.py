"""Attendance processing package."""
from .reader import read_records
from .stats import percentage, consecutive_absences
from .report import format_report
