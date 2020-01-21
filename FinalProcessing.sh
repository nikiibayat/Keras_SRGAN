ones=0
twos=0
for f in *; do
    if [ -d "$f" ]; then
        cd $f
        count=$(find -name '*.jpg' | wc -l)
	if [ $count -eq 1 ]
	then
		ones=$((ones+1))
	elif [ $count -eq 2 ]
	then
		twos=$((twos+1))
	else
	        mkdir "train"
        	mkdir "test"
        	mkdir "validation"
        	for img in *.jpg; do
           	if [ ! "$(ls -A test)" ]; then
                	echo test
			cp $img /home/nbayat5/celebA/CelebATest
                	mv $img test/
                	continue
           	fi
           	if [ ! "$(ls -A validation)" ]; then
                	echo validation
			cp $img /home/nbayat5/celebA/CelebAValidation
                	mv $img validation/
                	continue
           	fi
           	echo train
		cp $img /home/nbayat5/celebA/CelebATrain
		mv $img train/
        	done
	fi
	cd ../
    fi
done
echo ${ones} ones were discarded!
echo ${twos} twos were discarded!

