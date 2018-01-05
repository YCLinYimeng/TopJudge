# coding: UTF-8

import os
import json

in_path = "/data/disk1/private/zhonghaoxi/law/data"
out_path = "/data/disk1/private/zhonghaoxi/law/format_data"

num_process = 4
num_file = 20

from data_formatter import parse_sentence


def draw_out(in_path, out_path):
    print(in_path)
    inf = open(in_path, "r")
    ouf = open(out_path, "w")

    cnt = 0
    cx = 0
    for line in inf:
        try:
            data = json.loads(line)
            res = parse_sentence(data["content"], None)
            if not (data is None):
                data["content"] = res
                print(json.dumps(data), file=ouf)
                cnt += 1
                if cnt % 50000 == 0:
                    print(in_path, cnt, cx)
                    # break

        except Exception as e:
            pass  # print(e)
            # gg


def work(from_id, to_id):
    for a in range(int(from_id), int(to_id)):
        print(str(a) + " begin to work")
        draw_out(os.path.join(in_path, str(a)), os.path.join(out_path, str(a)))
        print(str(a) + " work done")


if __name__ == "__main__":
    import multiprocessing

    process_pool = []

    for a in range(0, num_process):
        process_pool.append(
            multiprocessing.Process(target=work, args=(a * num_file / num_process, (a + 1) * num_file / num_process)))

    for a in process_pool:
        a.start()

    for a in process_pool:
        a.join()
