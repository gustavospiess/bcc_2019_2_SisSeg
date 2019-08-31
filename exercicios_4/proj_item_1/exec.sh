
# Uploads a file
python3 upload.py --debug -u gustavo -c "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." -f TCC.txt

# Downloads a file
python3 download.py --debug -u gustavo -f TCC.txt

#Not existent file
python3 download.py --debug -u rovigo -f TCC.txt

#Read other users file
python3 download.py --debug -u rovigo -f ../gustavo/TCC.txt

#Write other users file
python3 upload.py --debug -u rovigo -f ../gustavo/TCC.txt -c ''

# clear it
rm gustavo/ -rf
rm rovigo/ -rf
rm users.csv
