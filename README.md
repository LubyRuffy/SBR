sudo apt-get install python-smbus
sudo apt-get install minidlna

curl http://localhost:5000/motor/R -d "speed=50&dir=FORWARD" -X PUT
