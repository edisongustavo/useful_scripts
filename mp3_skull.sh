#/bin/sh

#setup directories
mkdir temp
touch temp/urls.txt
touch temp/songs.html

#download song list and process it
curl http://mp3skull.com/mp3/$(echo $1 | tr " " "_").html > temp/songs.html
python src/main.py temp/songs.html temp/urls.txt

#Download each file. If the line starts with '#' that line won't be touched (i.e. won't download that file)
vi temp/urls.txt

trim() { echo $1; }

cat temp/urls.txt | while read line
do
	if [ ${line:0:1} != "#" ]
	then
		delimiterPos=`expr index "$line" ">>>"`
		filename=${line:0:delimiterPos-2}
		address=${line:delimiterPos+3}
		echo "Downloading $filename.mp3"
		curl $address > "$filename.mp3"
		
		#Check file size since the download may have failed for some reason
		tmpIFS=$IFS; IFS='\n';
		size=$(ls -l "$filename.mp3"  |awk -F " " '{ print $5 }')
		if [[ $(trim $size) == "0" ]]
		then
			echo "Download failed for "$filename". Deleting the file and appending it's name to log.txt"
			echo "$filename >>> $address\n" >> log.txt
			rm $filename.mp3
		fi
		IFS=$tmpIFS
	fi
done

echo "Finished all downloads. Thanks for using the downloader ;)"

#Clean up
rm -rf temp
