from session import Session
from datetime import datetime
import json
import pytz


def parse_data(file_name):
    db = dict()
    with open(file_name, 'r') as f:
        data = json.load(f)
        for d in data:
            if d['type'] == 'START':
                s = Session(d['id'], d['timestamp'])
                db[s.id] = s
            else:
                s = db[d['id']]
                s.end_time = d['timestamp']
                s.duration = int(s.end_time) - int(s.start_time)
                s.late = s.duration > 86400
                s.damaged = len(d['comments']) > 0
    return db


if __name__ == '__main__':
    local_tz = datetime.now().astimezone().tzinfo
    files = ['output_file', 'output_file_new']
    for file in files:
        dB = parse_data(file + ".txt")
        with open(file + "_result.txt", 'w') as f:
            headers = ['id', 'StartTime', 'EndTime', 'Duration', 'Late', 'Damaged']
            f.write('\t\t'.join(headers) + '\n')

            for (key, session) in dB.items():
                # utc_dt = datetime.utcfromtimestamp(int(session.start_time)).replace(tzinfo=pytz.utc)
                # sd_dt = utc_dt.astimezone(local_tz)
                # utc_dt = datetime.utcfromtimestamp(int(session.end_time)).replace(tzinfo=pytz.utc)
                # ed_dt = utc_dt.astimezone(local_tz)
                row = [
                    str(session.id),
                    # str(sd_dt),
                    session.start_time,
                    # str(ed_dt),
                    session.end_time,
                    str(session.duration),
                    str(session.late),
                    str(session.damaged)
                ]
                f.write("\t\t".join(row) + "\n")
