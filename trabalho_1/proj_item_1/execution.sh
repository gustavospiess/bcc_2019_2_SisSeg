python3 create.py -f temp.dmp -c "[1,2]" -i
echo "> temp.dmp file created"
echo --

python3 create.py -f temp.dmp -c "'asdf'" -i
echo --

python3 load.py -f temp.dmp  -i
echo --

rm temp.dmp
echo "> temp.dmp file deleted"
