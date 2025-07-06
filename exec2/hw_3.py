import re

def is_valid_email(s: str) -> bool:
    email_pattern = r'^(?!@)[^@]*@[^@]*\.(com|cn)$'
    return re.fullmatch(email_pattern, s) is not None