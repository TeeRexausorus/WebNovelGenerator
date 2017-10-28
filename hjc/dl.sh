mkdir input

#http://www.wuxiaworld.com/hjc-index/hjc-chapter-21-1/
i=167;
k=1;
if ! [ -f ./input/hjc-chapter-$i-$k ]; then
    wget http://www.wuxiaworld.com/hjc-index/hjc-chapter-$i-$k/ -O input/hjc-chapter-$i-$k;
fi
res=$?
while [ $res -eq 0 ]; do
    while [ $res -eq 0 ]; do
	k=$((k+1))
	if ! [ -f ./input/hjc-chapter-$i-$k ]; then
	    wget http://www.wuxiaworld.com/hjc-index/hjc-chapter-$i-$k/ -O input/hjc-chapter-$i-$k;
	fi
	res=$?
	if [ $res -ne 0 ]; then
	    rm -f input/hjc-chapter-$i-$k
	fi
    done
    k=1
    i=$((i+1))
    if ! [ -f ./input/hjc-chapter-$i-$k ]; then
	wget http://www.wuxiaworld.com/hjc-index/hjc-chapter-$i-$k/ -O input/hjc-chapter-$i-$k;
    fi
    res=$?
    if [ $res -ne 0 ]; then
	rm -f input/hjc-chapter-$i-$k
    fi
done
#for i in `seq 1 280`; do echo $i; done
