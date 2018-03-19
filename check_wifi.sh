#!/bin/bash

LOG_DIR=/var/log/
LOG=kern.log
cd $LOG_DIR

while :
  do
    OUTPUT="$(tail -n 50 $LOG | grep WLC_SCAN)"
    if [[ $OUTPUT = *"error (-22)" ]];
    then
      echo $OUTPUT
      echo $OUTPUT >> ~/error_log/wifi_crash.txt
      rfkill list
      echo "WiFi Kernel error (-22) occured Please hardset WiFi NIC."      
      break
    fi
  done

  


