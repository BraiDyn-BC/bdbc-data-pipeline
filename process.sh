#/bin/bash
source env.sh

BATCH=${1:?}

ENVCHECK=$(printenv | grep BDBC_TEMP_LOG_DIR | wc -w)
if test $ENVCHECK -eq 0; then
    echo "specify BDBC_TEMP_LOG_DIR"
    exit 1
fi

LOGDIR=$BDBC_TEMP_LOG_DIR
if test -d $LOGDIR; then
    :
else
    mkdir -p $LOGDIR
fi

LOGFILE="$LOGDIR/package_${BATCH}_$(date +'%Y%m%d-%H%M%S').txt"
echo "logging into: $LOGFILE"

date +"started processing at: %Y-%m-%d %H:%m:%s" >>$LOGFILE
echo "" >>$LOGFILE

if package-nwb -B $BATCH 2>&1 | tee -a $LOGFILE; then
    echo "" >>$LOGFILE
    date +"finished processing at: %Y-%m-%d %H:%m:%s" | tee -a $LOGFILE
else
    echo "" >>$LOGFILE
    date +"aborted processing at: %Y-%m-%d %H:%m:%s" | tee -a $LOGFILE
fi

