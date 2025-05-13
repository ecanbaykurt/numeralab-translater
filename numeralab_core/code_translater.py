import re

def translate_fortran_to_python(fortran_code):
    python_code = fortran_code

    python_code = re.sub(r'c\s+', '# ', python_code)
    python_code = re.sub(r'dimension ', '# dimension -> use numpy arrays in Python\n# ', python_code)
    python_code = re.sub(r'double precision', '# double precision -> use float (numpy float64)', python_code)
    python_code = re.sub(r'data (.+?)/(.+?)/', r'# data \1 = \2  # Needs manual conversion', python_code)
    python_code = re.sub(r'open\s*\(.*?file\s*=\s*\'(.+?)\'\)', r"# open file '\1' # Use open() in Python", python_code)
    python_code = re.sub(r'write\(6,.*?\)', '# print()', python_code)
    python_code = re.sub(r'format\(.*?\)', '# Format string not directly portable, rewrite needed', python_code)
    python_code = re.sub(r'do (\d+) (\w+)=(.+?),(.+?)', r'for \2 in range(int(\3), int(\4)+1):', python_code)
    python_code = re.sub(r'end do', '# End of for loop', python_code)
    python_code = re.sub(r'stop', 'exit()', python_code)
    python_code = re.sub(r'end', '# End of code block', python_code)
    python_code = re.sub(r'call (\w+)', r'\1()', python_code)
    python_code = re.sub(r'subroutine (\w+)', r'def \1():', python_code)

    return python_code
