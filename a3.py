filename = $1
firstline = $2
lastline = $3

i = 0
exec <${filename}  # redirect file into our stdin
while read
do    # read each line into REPLY variable
i = $(($i+1))  # maintain line count
if ["$i"-ge "${firstline}"]:
    then
if ["$i"-gt "${lastline}":
    then
      break
    else
      echo "${REPLY}"
    fi
  fi
done
