def valid_username(value):
    if not all(ch.isalnum() or ch == '_' for ch in value):
        raise ValueError('Ensure this value contains only letters, numbers and underscore.')