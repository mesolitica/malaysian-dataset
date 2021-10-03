import subprocess

en = 'However, the 1,643-year-old empire collapsed in the early 19th century following wars and pressures from the Annam Government that emerged in northern Vietnam and southern China.'
ms = 'Bagaimanapun, empayar berusia 1,643 tahun itu jatuh pada awal abad ke-19 berikutan peperangan dan tekanan daripada Kerajaan Annam yang muncul di utara Vietnam dan selatan China.'
with open('en.small', 'w') as fopen:
    fopen.write(en)

with open('ms.small', 'w') as fopen:
    fopen.write(ms)

cmd = 'python3 align.py -s en.small -t ms.small --priors align.priors --model 3 -f out.f -r out.r'
subprocess.run(cmd.split())
