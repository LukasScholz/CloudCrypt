pip uninstall cloudcrypt -y
rm -r ./dist
python -m build
pip install cloudcrypt --no-index --find-links ./dist


## Upload
#twine check dist/*
#twine upload -r testpypi dist/*