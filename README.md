# Wiki Workload

A method for calculating user workload based on MediaWiki page history text and incremental compression.

## Usage

```sh
mkdir wiki-dump
cd wiki-dump

python -m venv .venv
source .venv/bin/activate

pip install poetry

git clone https://github.com/mediawiki-client-tools/mediawiki-dump-generator
cd mediawiki-dump-generator

poetry update && poetry install && poetry build

pip install --force-reinstall dist/*.whl

cd ..

# Don't forget to delete the command from the command history after running it. Alternatively, if you've configured it accordingly, add a space before the command to prevent it from being recorded in the command history.
 dumpgenerator \
    --api "https://WIKI/api.php" \
    --index "https://WIKI/index.php" \
    --xml \
    --xmlrevisions \
    --images \
    --user "USERNAME" \
    --pass "PASSWORD"

pip install mwxml

python 1.py WIKI-20260423-wikidimp/WIKI-20260423-history.xml
python 2.py
```
