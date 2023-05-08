#!/bin/bash

tophap_path = $1
public_path = $2
out_path = $3

if [ ! -d $out_path"/matkData" ]; then
  mkdir $out_path"/matkData"
fi

java -jar MATK-1.0.jar -peakCalling -ip $tophap_path"/ip/accepted_hits.bam" -input $tophap_path"/input/accepted_hits.bam" -out $out_path"/matkData/peak.bed"
java -jar MATK-1.0.jar -quantification -ip $tophap_path"/ip/accepted_hits.bam" -input $tophap_path"/input/accepted_hits.bam" -bed $out_path"/matkData/peak.bed" -gtf $public_path"ensemblData/Homo_sapiens.GRCh38.86.chr.gtf" -out $out_path"/matkData/m6A_quantification.bed"
