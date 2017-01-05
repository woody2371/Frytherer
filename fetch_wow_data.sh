echo -n "wow_chieves = " > wow_db_data_test.py
wget -O "wow_chieves_output.json" "https://us.api.battle.net/wow/data/character/achievements?locale=en_US&apikey=xdpn92p4esktsj38bx2hp38c4bwsar7h"
sed -i 's/true/True/g' wow_chieves_output.json
sed -i 's/false/False/g' wow_chieves_output.json
cat wow_chieves_output.json >> wow_db_data_test.py

echo -n "wow_realms = " >> wow_db_data_test.py
wget -O "wow_realms_output.json" "https://us.api.battle.net/wow/realm/status?locale=en_US&apikey=xdpn92p4esktsj38bx2hp38c4bwsar7h"
sed -i 's/true/True/g' wow_realms_output.json
sed -i 's/false/False/g' wow_realms_output.json
cat wow_realms_output.json >> wow_db_data_test.py

echo -n "wow_talents = " >> wow_db_data_test.py
wget -O "wow_talents_output.json" "https://us.api.battle.net/wow/data/talents?locale=en_US&apikey=xdpn92p4esktsj38bx2hp38c4bwsar7h"
sed -i 's/true/True/g' wow_talents_output.json
sed -i 's/false/False/g' wow_talents_output.json
cat wow_talents_output.json >> wow_db_data_test.py
