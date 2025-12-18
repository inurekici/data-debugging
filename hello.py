# pylint: disable=missing-docstring

import sys

def full_name(first_name, last_name):
   # breakpoint() # equivalent to `ipdb.set_trace()`
    name = f"{first_name.capitalize()} {last_name.capitalize()}"
# tek isim girdiğinde boşluklu döndüğü için testten kaldı, o yüzden buraya strip() ekleyerek
# boşlukları silmesini rica ettim
    return name.strip()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # => ['hello.py']
        print(f'Hello{full_name("", "")}!')
    elif len(sys.argv) == 2:
        # => ['hello.py', 'John' ]
        print(f'Hello {full_name(sys.argv[1], "")}!')
    else:
        # => ['hello.py', 'John', 'Lennon']
        print(f"Hello {full_name(sys.argv[1], sys.argv[2])}!")
