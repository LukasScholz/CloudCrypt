cd ..
rm -r ./dist
python -m build
pip install cloudcrypt --no-index --find-links ./dist