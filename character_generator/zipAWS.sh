cd "/Users/AntonBriganti/Documents/D&D STUFF/dnd_python_projects/character_generator/"
cp $(find *.py) aws_files/
cp -a srd_data/. aws_files/srd_data/
cd aws_files/
rm -rf ~/character_creator.zip
zip -r9 ~/character_creator.zip .
