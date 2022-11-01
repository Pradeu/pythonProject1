def record_generate():
    cur_record = 0
    max_record = open("Record.txt", mode="w+")

    if int(max_record.readline()) < cur_record:
        max_record.write(str(cur_record))
