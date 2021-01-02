#!/bin/bash

accessLogFile="/var/log/nginx/access.log"


ipStat(){
	tail -n $num $accessLogFile |awk '{a[$1]++}; END{for(i in a) { printf("%s\t%s\n", a[i], i); }}' | sort -n -r| head -10
}

purgeIp(){
	tail -n $num $accessLogFile |awk -v hits=$hits '{a[$1]++}; END{for(i in a) { if(a[i]>hits){ print(i) }}}' | sort -n -r| head -10 > purgeIp.conf
    exec < purgeIp.conf
    read ip
	iptables -A INPUT -s $ip -j DROP
}

usage(){
	echo "Usage: drop top hits IP address"
	echo " -n	Last lines num"
	echo " -d	Hit num"
	echo " -h   Display usage information"
	exit 1
}


while getopts n:d:h option
  do case "${option}" in
    n) num=$OPTARG; ipStat;;
    d) hits=$OPTARG; purgeIp;;
    h) usage;;
  esac
done

if [ $# -eq 0 ];then
	usage
	exit 0
fi