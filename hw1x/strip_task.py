def strip(inname, outname):
    with open(inname, 'r') as file_in:
        with open(outname, 'w') as file_out:
            for s in file_in:
                if '[strip]' not in s:
                    file_out.write(s)
