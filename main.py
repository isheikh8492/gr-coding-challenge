from session import Summary
from datetime import datetime
import json
import pytz


def parse_data(file_name):
    db = dict()
    with open(file_name, 'r') as f:
        data = json.load(f)
        for d in data:
            if d['type'] == 'START':
                s = Summary(d['id'], d['timestamp'])
                db[s.id] = s
            else:
                s = db[d['id']]
                s.end_time = d['timestamp']
                s.duration = int(s.end_time) - int(s.start_time)
                s.late = s.duration > 86400
                s.damaged = len(d['comments']) > 0
    # local_tz = datetime.now().astimezone().tzinfo
    output_file_name = file_name.split('.')[0] + "_result.txt"
    with open(output_file_name, 'w') as f:
        headers = ['id', 'StartTime', 'EndTime', 'Duration', 'Late', 'Damaged']
        f.write('\t\t'.join(headers) + '\n')

        for (key, session) in db.items():
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
    return output_file_name


if __name__ == '__main__':
    files = ['output_file', 'output_file_new']
    for file in files:
        parse_data(file + ".txt")
