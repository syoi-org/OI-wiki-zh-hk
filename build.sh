#/usr/bin/env bash
pipenv install
cp -r OI-wiki OI-wiki-zh-hk
pipenv run python translate.py OI-wiki-zh-hk
pushd OI-wiki-zh-hk
./scripts/pre-build/install-theme-vendor.sh
pipenv install
pipenv run mkdocs build
popd
mv OI-wiki-zh-hk/site build
