from primos import is_Prime
import sys
import os

def main():
    n = 5
    print(123134556245634652611123142341
          , is_Prime(123134556245634652611123142341))
    def find_files(search_path):
        result = []

    # Wlaking top-down from the root
        for root, dir, files in os.walk(search_path):
            print(files)
            # if filename in files:
            #     result.append(os.path.join(root, filename))
    print()
    [print(f) for f in sys.path]
if __name__ == "__main__":
     main()