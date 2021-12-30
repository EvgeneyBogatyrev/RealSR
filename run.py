import os
from pathlib import Path

os.system("chmod -R 0777 /model")

with open('/model/run.sh', 'w') as f:

    videos = os.listdir('/dataset')
    f.write('mkdir /model/result\n')

    for video in videos:
        f.write(f'mkdir /model/result/{video}\n')
        f.write(f'python3 /model/codes/test.py -opt /model/codes/options/df2k/test_df2k.yml -in_path /dataset/{video} -res_path /model/result/{video}\n')

    f.write('chmod -R 0777 /model/result\n')

os.system("chmod -R 0777 /model")
os.system('/model/run.sh')
