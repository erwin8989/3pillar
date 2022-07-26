echo TIME = $(date)
echo MEMORY = $(free -m | awk 'NR==2{printf "%.2f%%\t\t", $3*100/$2 }')
echo DISK = $(df -h | awk '$NF=="/"{printf "%s\t\t", $5}')
echo CPU = $(top -bn1 | grep load | awk '{printf "%.2f%%\t\t\n", $(NF-2)}')chmod +x system_stats.sh
echo 

