import io
from pathlib import Path
import __main__

DEFAULT_INPUT_FILE = 'input.txt'

def get_input_path() -> str:
    return Path(__main__.__file__).with_name(DEFAULT_INPUT_FILE)

def get_input_file(_test_str=None):
    if _test_str:
        return io.StringIO(_test_str)
    else:
        return open(get_input_path())


def get_input_lines(_test_str=None):
    with get_input_file(_test_str) as f:
        while True:
            try:
                yield next(f).strip()
            except StopIteration:
                break

def get_input_chunks_by_size(size=3, _test_str=None):
    with get_input_file(_test_str) as f:
        while True:
            try:
                yield [next(f).strip() for _ in range(size)]
            except StopIteration:
                break

def get_input_chunks_by_separator(separator='', _test_str=None):
    with get_input_file(_test_str) as f:
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
