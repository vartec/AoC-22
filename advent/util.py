import io
from pathlib import Path
import __main__

DEFAULT_INPUT_FILE = 'input.txt'

def get_input_path() -> str:
    return Path(__main__.__file__).with_name(DEFAULT_INPUT_FILE)

def get_input_lines():
    with open(get_input_path()) as f:
        while True:
            try:
                yield next(f).strip()
            except StopIteration:
                break

def get_input_chunks_by_size(size=3):
    with open(get_input_path()) as f:
        while True:
            try:
                yield [next(f).strip() for _ in range(size)]
            except StopIteration:
                break

def get_input_chunks_by_separator(separator=''):
    with open(get_input_path()) as f:
        chunk = []
        for line in f:
            line = line.strip()
            if line != separator:
                chunk.append(line)
            else:
                yield chunk
                chunk = []
        if chunk:
            yield chunk
