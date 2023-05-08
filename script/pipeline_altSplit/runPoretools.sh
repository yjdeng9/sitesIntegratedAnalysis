#bin/bash
input=$1
output=$2
#input=/data/dengyongjie/altSplicing/datas/basecallingData/workspace/pass/
#output=/data/dengyongjie/altSplicing/datas/fastqData/
for file in $input*;do 
	if [ -d $file ];then
		file_num=${file/"$input"/""}
		out_file=$output"batch_"$file_num".fastq"
		poretools fastq $file >$out_file	
		echo $out_file
	fi
done
