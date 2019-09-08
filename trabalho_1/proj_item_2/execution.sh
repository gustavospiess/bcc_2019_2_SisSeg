python3 create.py -f temp.json -c "[1,2]" -i
echo "> temp.json file created"
echo --

python3 create.py -f temp.json -c "'asdf'" -i
echo --

python3 load.py -f temp.json  -i
echo --

rm temp.json
echo "> temp.json file deleted"
