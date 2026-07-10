from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():
    working_dir = "calculator"

    print(run_python_file(working_dir, "main.py", ["3 + 5"]))

    # print(run_python_file(working_dir, "tests.py"))
    # print(run_python_file(working_dir, "../main.py"))
    # print(run_python_file(working_dir, "nonexistent.py"))
    # print(write_file(working_dir, "lorem.txt", "This is a test content for the new file."))
    # print(write_file(working_dir, "pkg/morelorem.txt", "This is a test content for the new file."))
    # print(write_file(working_dir, "/tmp/temp.txt", "This is a test content for the new file."))

    # print(get_file_content(working_dir, "lorem.txt"))
    # print(get_file_content(working_dir, "main.py"))
    # print(get_file_content(working_dir, "pkg/calculator.py"))
    # print(get_file_content(working_dir, "pkg/notexists.py"))
    # print(get_file_content(working_dir, "/bin/cat"))
    # root_contents = get_files_info(working_dir)
    # print("Root Directory Contents:")
    # print(root_contents)
    # pkg_contents = get_files_info(working_dir, "pkg")
    # print("\n'pkg' Directory Contents:")
    # print(pkg_contents)
    # bin_contents = get_files_info(working_dir, "/bin")
    # print("\n'bin' Directory Contents:")
    # print(bin_contents)
    # other_contents = get_files_info(working_dir, "../")
    # print("\n'../' Directory Contents:")
    # print(other_contents)

main()