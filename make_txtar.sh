rm -rf /tmp/noblemask

rm -f /tmp/noblemask.tar
rm -f /tmp/filelist.txt

pytest >pytest.log 2>&1

{
    rg --files --glob='*.log'
    rg --files |
        grep -viE '\.(txt|rst|cfg|toml|ini)' |
        grep -viE 'Makefile|conftest|setup|test_skeleton|conf\.py|__init__.py' |
        grep -v make_txtar.sh |
        grep -v module_aa.py |
        grep -v module_aaa.py |
        grep -v module_aaaa.py |
        grep -v module_aaaaa.py |
        grep -v module_aaaaaa.py |
        grep -v README.org

} | tee /tmp/filelist.txt

tar -cf /tmp/noblemask.tar -T /tmp/filelist.txt
mkdir -p /tmp/noblemask
tar xf /tmp/noblemask.tar -C /tmp/noblemask
rg --files /tmp/noblemask
txtar-c /tmp/noblemask | pbcopy
