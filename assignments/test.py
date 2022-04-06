import filecmp
import os
import sys


TEST_FOLDER = "tests"


def load_files(folder):
    in_files = []
    ans_files = []

    for entry in os.listdir(folder):
        if entry.endswith(".a"):
            ans_files.append(entry)
        elif not entry.endswith(".out"):
            in_files.append(entry)

    return sorted(in_files), sorted(ans_files)


def load_source_code(folder):
    for entry in os.listdir(folder):
        if entry.endswith(".py"):
            return entry
    raise FileNotFoundError(f"No .py file found in {folder}")


def evaluate(in_file, out_path, ans_path):
    out_str = open(out_path).readline()
    ans_str = open(ans_path).readline()

    if out_str != ans_str:
        print(f"Failed test: {in_file}")
        print(f"Expected:{ans_str.strip()}")
        print(f"Output:{out_str.strip()}")
        print("--------------------------")
        return False
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Usage: py test.py <task_folder>")
    folder = sys.argv[1]
    test_folder = os.path.join(folder, TEST_FOLDER)

    source_code = load_source_code(folder)
    in_files, ans_files = load_files(test_folder)
    num_tests = len(in_files)
    print(f"Testing code {source_code} against {num_tests} tests")

    num_pass = 0
    for in_file, ans_file in zip(in_files, ans_files):
        source_code_path = os.path.join(folder, source_code)
        in_path = os.path.join(test_folder, in_file)
        out_path = os.path.join(test_folder, f"{in_file}.out")
        ans_path = os.path.join(test_folder, f"{in_file}.a")

        os.system(f"python {source_code_path} < {in_path} > {out_path}")
        num_pass += evaluate(in_file, out_path, ans_path)

    num_fail = num_tests - num_pass
    if num_fail:
        print(f"Failed {num_fail} / {num_tests} tests")
    else:
        print("Passed all tests. Good job!")
