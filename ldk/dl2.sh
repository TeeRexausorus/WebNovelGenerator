mkdir -p input

function dl {
    if ! [ -f ./input/ldk-chapter-$1 ]; then
	wget http://www.wuxiaworld.com/ldk-index/ldk-chapter-$1 -O input/ldk-chapter-$1;
    fi
}

    i=1;
    dl $i
    res=$?
    while [ $res -eq 0 ]; do
	i=$((i+1))
	dl $i
	res=$?
	if [ $res -ne 0 ]; then
	    rm -f input/ldk-chapter-$i

	fi
    done
