def strip(inname, outname):
    file_in = open(inname, 'r')
    file_out = open(outname, 'w')
    for str in file_in:
        if str.find('[strip]') == -1:
            file_out.write(str)
