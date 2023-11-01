def comptage(in_filename, out_filename):
    with open(in_filename, 'r', encoding="utf-8") as re, open(out_filename, 'w', encoding='utf-8') as wr:
        for counter, line in enumerate(re):
            wr.write(':'.join([str(counter + 1), str(len(line.split())), str(len(line)), line]))


comptage('files/samplefile_1.txt', 'files/outsample1.txt')
