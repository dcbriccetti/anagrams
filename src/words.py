def words_from_file(filename: str):
    with open(filename) as file:
        return [line.strip().lower() for line in file if not line.startswith('#')]
