#/usr/bin/bash
DSOCOUNT=$(wc -l < /u01/git/jobs/remote_hist.csv)
ACOUNT=$(head -n 1 /u01/git/jobs/account)

echo "$DSOCOUNT" > acount

if [ "$DSOCOUNT" -gt "$ACOUNT" ]; then
    echo "$DSOCOUNT" > acount
    /u01/distr/tlg/telegram -t 1152884180:AAEzbinHoNosvrgNQO7y_A_Fm0Ta_jVo1Vg -c -1001376744472 "started install num $DSOCOUNT"
fi
