mkdir input

#http://www.wuxiaworld.com/wmw-index/wmw-chapter-231/
i=1;
if ! [ -f ./input/ast-chapter-$i ]; then
    wget http://www.wuxiaworld.com/ast-index/ast-chapter-$i/ -O input/ast-chapter-$i;
fi
res=$?
while [ $res -eq 0 ]; do
    i=$((i+1))
    if ! [ -f ./input/ast-chapter-$i ]; then
		wget http://www.wuxiaworld.com/ast-index/ast-chapter-$i/ -O input/ast-chapter-$i;
    fi
    res=$?
    if [ $res -ne 0 ]; then
		rm -f input/ast-chapter-$i
    fi
done
#for i in `seq 1 280`; do echo $i; done
