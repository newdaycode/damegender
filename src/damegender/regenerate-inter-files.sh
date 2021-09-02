#!/usr/bin/sh

#  Copyright (C) 2021 David Arroyo Menéndez

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.



echo "Building interfemales.csv"
python3 mergeinterfiles.py --file1="files/names/names_at/atfemales.csv" --file2="files/names/names_au/aufemales.csv" --output=files/tmp/ataufemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataufemales.csv" --file2="files/names/names_be/befemales.csv" --output=files/tmp/ataubefemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubefemales.csv" --file2="files/names/names_ca/cafemales.csv" --output=files/tmp/ataubecafemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecafemales.csv" --file2="files/names/names_de/defemales.csv" --output=files/tmp/ataubecadefemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadefemales.csv" --file2="files/names/names_dk/females.csv" --output=files/tmp/ataubecadedkfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkfemales.csv" --file2="files/names/names_es/esfemeninos.csv" --output=files/tmp/ataubecadedkesfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfemales.csv" --file2="files/names/names_fi/fifemales.csv" --output=files/tmp/ataubecadedkesfifemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfifemales.csv" --file2="files/names/names_ie/iefemales.csv" --output=files/tmp/ataubecadedkesfiiefemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiiefemales.csv" --file2="files/names/names_is/isfemales.csv" --output=files/tmp/ataubecadedkesfiieisfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieisfemales.csv" --file2="files/names/names_mx/mujeres.csv" --output=files/tmp/ataubecadedkesfiieismxfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxfemales.csv" --file2="files/names/names_nz/nzfemales.csv" --output=files/tmp/ataubecadedkesfiieismxnzfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzfemales.csv" --file2="files/names/names_pt/ptfemales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptfemales.csv" --file2="files/names/names_si/sifemales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsifemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsifemales.csv" --file2="files/names/names_us/usfemales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusfemales.csv" --file2="files/names/names_uy/uyfemeninos.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusuyfemales.csv" --file2="files/names/names_fr/frfemales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfrfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusuyfrfemales.csv" --file2="files/names/names_ch/chfemales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchfemales.csv



echo "Building intermales.csv"
python3 mergeinterfiles.py --file1="files/names/names_at/atmales.csv" --file2="files/names/names_au/aumales.csv" --output=files/tmp/ataumales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataumales.csv" --file2="files/names/names_be/bemales.csv" --output=files/tmp/ataubemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubemales.csv" --file2="files/names/names_ca/camales.csv" --output=files/tmp/ataubecamales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecamales.csv" --file2="files/names/names_de/demales.csv" --output=files/tmp/ataubecademales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecademales.csv" --file2="files/names/names_dk/males.csv" --output=files/tmp/ataubecadedkmales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkmales.csv" --file2="files/names/names_es/esmasculinos.csv" --output=files/tmp/ataubecadedkesmales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesmales.csv" --file2="files/names/names_fi/fimales.csv" --output=files/tmp/ataubecadedkesfimales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfimales.csv" --file2="files/names/names_ie/iemales.csv" --output=files/tmp/ataubecadedkesfiiemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiiemales.csv" --file2="files/names/names_is/ismales.csv" --output=files/tmp/ataubecadedkesfiieismales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismales.csv" --file2="files/names/names_mx/hombres.csv" --output=files/tmp/ataubecadedkesfiieismxmales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxmales.csv" --file2="files/names/names_nz/nzmales.csv" --output=files/tmp/ataubecadedkesfiieismxnzmales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzmales.csv" --file2="files/names/names_pt/ptmales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptmales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptmales.csv" --file2="files/names/names_si/simales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsimales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsimales.csv" --file2="files/names/names_us/usmales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusmales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusmales.csv" --file2="files/names/names_uy/uymasculinos.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuymales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusuymales.csv" --file2="files/names/names_fr/frmales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfrmales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusuyfrmales.csv" --file2="files/names/names_ch/chmales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchmales.csv

mv files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchmales.csv files/names/names_inter/intermales.csv
mv files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchfemales.csv files/names/names_inter/interfemales.csv

echo "Cleaning temporal files"
rm files/tmp/*
