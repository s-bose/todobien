from datetime import date


def check_date(date_str: str) -> bool:
    try:
        date.fromisoformat(date_str)
        return True
    except ValueError:
        return False


def validate_path(path: str):
    pass
