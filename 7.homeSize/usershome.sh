awk -F: '{print $1,$6}' /etc/passwd
awk -F: '{print $6}' /etc/passwd

