mkdir input
for j in `seq 1 16`; do
    i=1;
    k=1;
    if ! [ -f ./input/ti-vol-$j-chapter-$i-$k ]; then
	wget http://www.wuxiaworld.com/ti-index/ti-vol-$j-chapter-$i-$k -O input/ti-vol-$j-chapter-$i-$k;
    fi
    res=$?
    while [ $res -eq 0 ]; do
	while [ $res -eq 0 ]; do
	    k=$((k+1))
	    if ! [ -f ./input/ti-vol-$j-chapter-$i-$k ]; then
		wget http://www.wuxiaworld.com/ti-index/ti-vol-$j-chapter-$i-$k -O input/ti-vol-$j-chapter-$i-$k
	    fi
	    res=$?
	    if [ $res -ne 0 ]; then
		rm -f input/ti-vol-$j-chapter-$i-$k
	    fi
	done
	k=1
	i=$((i+1))
	if ! [ -f ./input/ti-vol-$j-chapter-$i-$k ]; then
	    wget http://www.wuxiaworld.com/ti-index/ti-vol-$j-chapter-$i-$k -O input/ti-vol-$j-chapter-$i-$k;
	fi
	res=$?
	if [ $res -ne 0 ]; then
	    rm -f input/ti-vol-$j-chapter-$i-$k
	
	fi
    done
done

#for i in `seq 1 280`; do echo $i; done
