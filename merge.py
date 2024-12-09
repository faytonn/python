import sys
def merge(file1Path, file2Path, outputPath, case=False):
    with open(file1Path, 'r') as file1, open(file2Path, 'r') as file2, open(outputPath, 'w') as output:
        line1 = file1.readline()
        line2 = file2.readline()
        while line1 or line2:
            if not line1:
                output.write(line2)
                line2 = file2.readline()
            elif not line2:
                output.write(line1)
                line1 = file1.readline()
            else:
                if case:
                    content1 = line1.strip().lower()
                    content2 = line2.strip().lower()
                else:
                    content1 = line1.strip()
                    content2 = line2.strip()
                if content1 <= content2:
                    output.write(line1)
                    line1 = file1.readline()
                else:
                    output.write(line2)
                    line2 = file2.readline()
def main():
    if len(sys.argv) < 4:
        sys.exit(1)
    caseSensitive = False
    if sys.argv[1] == '-i':
        caseSensitive = True
        file1 = sys.argv[2]
        file2 = sys.argv[3]
        output = sys.argv[4]
    else:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        output = sys.argv[3]
    merge(file1, file2, output, caseSensitive)
if __name__ == "__main__":
    main()