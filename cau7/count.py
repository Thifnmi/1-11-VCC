import os
import csv
import re
from threading import Thread
import time
from multiprocessing import Process


def filler_content(contents):
    delimiters = '.', '\xa0', '?', '!', '(', ')', '|', ':',
    ', ', '  ', '"', ' – ', ',…', ': ', '/', ' / ', '\xa0', '…'
    regex_pattern = "|".join(map(re.escape, delimiters))
    data = " ".join(re.split(regex_pattern, contents))
    # print(data)
    return data


def counter(contents):
    # print(contents)
    dict_words = {}
    for content in str(contents).split(" "):
        if content in dict_words:
            dict_words[content] = dict_words[content] + 1
        else:
            dict_words[content] = 1
    return dict_words


def write_file(file_name, dict_words):
    file_out = open(file_name, "w", encoding="utf-8")
    for word, value in dict_words.items():
        # string = f"{word}: {value}"
        # print(string)
        file_out.write('%s: %s\n' % (word, value))
    file_out.close()


def open_file_thread(filecsv):
    with open(filecsv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        line = 0
        contents = []
        for row in reader:
            if line == 0:
                line += 1
                continue
            else:
                raw_name = re.sub('\W+', '', row[1])
                contents.append(row[2])
                # print(raw_name, row[2])
                line += 1

        file_name = "count_with_thread\\" + raw_name + ".txt"
        data = filler_content(str(contents))
        dict_words = counter(data)
        # print(dict_words)
        write_file(file_name, dict_words)


def open_file_process(filecsv):
    with open(filecsv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        line = 0
        contents = []
        for row in reader:
            if line == 0:
                line += 1
                continue
            else:
                raw_name = re.sub('\W+', '', row[1])
                contents.append(row[2])
                # print(raw_name, row[2])
                line += 1

        file_name = "count_with_process\\" + raw_name + ".txt"
        data = filler_content(str(contents))
        dict_words = counter(data)
        # print(dict_words)
        write_file(file_name, dict_words)


# print(len(os.listdir(os.getcwd()+"/result_Process")))
def default():
    for filename in os.listdir(os.getcwd()+"\\result_Thread"):
        # print(filename)
        with open(os.path.join(os.getcwd()+"\\result_Thread", filename), 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            line = 0
            contents = []
            for row in reader:
                if line == 0:
                    line += 1
                    continue
                else:
                    raw_name = re.sub('\W+', '', row[1])
                    contents.append(row[2])
                    # print(raw_name, row[2])
                    line += 1

            file_name = "count_with_thread\\" + raw_name + ".txt"
            data = filler_content(str(contents))
            dict_words = counter(data)
            # print(dict_words)
            write_file(file_name, dict_words)


def file_thread():
    t1 = time.perf_counter()
    threads = []
    for filecsv in os.listdir(os.getcwd()+"\\result_Thread"):
        filecsv = os.getcwd()+"\\result_Thread\\" + filecsv
        t = Thread(target=open_file_thread, args=[filecsv])
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    print(f"Done with thread in {time.perf_counter() - t1} second(s)")


def file_process():
    t1 = time.perf_counter()
    processes = []
    for filecsv in os.listdir(os.getcwd()+"\\result_Thread"):
        filecsv = os.getcwd()+"\\result_Thread\\" + filecsv
        p = Process(target=open_file_process, args=[filecsv])
        p.start()
        processes.append(p)
    for process in processes:
        process.join()
    print(f"Done with process in {time.perf_counter() - t1} second(s)")


file_thread()
file_process()
