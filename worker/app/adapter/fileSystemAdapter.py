import uuid

extensions = {
    'python': '.py',
    'java': '.java',
    'c': '.c',
    'javascript': '.js'
}


def write_content_in_random_file(content: str, language: str) -> str:
    random_name = str(uuid.uuid4())
    full_file_name = f'{random_name}-{language}.{extensions[language]}'
    with open(full_file_name, 'w') as f:
        f.write(content)
    return full_file_name
