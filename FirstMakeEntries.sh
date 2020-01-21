input="identity_CelebA.txt"
while IFS= read -r line
do
  echo $line
  stringarray=($line)
  img=${stringarray[0]}
  folder=${stringarray[1]}
  foldername="identities/${folder}/"
  mkdir -p $foldername
  cp img_align_celeba/$img $foldername
done < "$input"
