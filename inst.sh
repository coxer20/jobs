#/usr/bin/bash
DSOCOUNT=$(wc -l < /u01/git/jobs/remote_hist.csv)
ACOUNT=$(head -n 1 /u01/git/jobs/acount)

sshpass -p asdf3 ssh puser@10.203.92.232 cat /u01/gnu/eksportal.org/public_page/history.csv > /u01/git/jobs/remote_hist.csv

if [ "$DSOCOUNT" -gt "$ACOUNT" ] || [ "$DSOCOUNT" -lt "$ACOUNT" ]; then
    echo "$DSOCOUNT" > /u01/git/jobs/acount
    /u01/distr/tlg/telegram -t 1152884180:AAEzbinHoNosvrgNQO7y_A_Fm0Ta_jVo1Vg -c -1001376744472 "started install num $DSOCOUNT"
fi
