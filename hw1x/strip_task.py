def strip(inname, outname):
    file_in = open(inname, 'r')
    file_out = open(outname, 'w')
    for s in file_in:
        if '[strip]' not in s:
            file_out.write(s)
    file_in.close()
    file_out.close()
