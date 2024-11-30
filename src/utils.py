def get_input(file_path: str) -> str:
    """
    Grab the input file downloaded from advent of code
    """
    with open(file_path) as f:
        text = f.read()

    return text
