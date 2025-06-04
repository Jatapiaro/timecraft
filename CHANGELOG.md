# 📋 Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [0.5.0] - 2025-06-04

### Added
- `start_of_week(from_date, week_start)` to calculate week start from a given date.
- `end_of_week(from_date, week_start)` to get the week's end.
- `yesterday(from_date)` and `tomorrow(from_date)` for simple date deltas.
- `Day` enum for explicit weekday handling.
- Internal normalization utilities (`_normalize_week_inputs`, `_add_days_to_date`).
- Full test coverage using `pytest`.

---

## [Unreleased]

### Planned
- `next_weekday`, `previous_weekday` utilities.
- `week_of`, `weeks_between`.
- `first_day_of_month`, `last_day_of_month`.