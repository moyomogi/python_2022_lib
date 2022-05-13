[![Netlify Status](https://api.netlify.com/api/v1/badges/372f004b-ea59-4ba2-bbbf-2d5f6213fffd/deploy-status)](https://app.netlify.com/sites/python-2022-lib/deploys)
[![Actions Status](https://github.com/moyomogi/python_2022_lib/actions/workflows/deploy.yml/badge.svg)](https://github.com/moyomogi/python_2022_lib/actions)
[![license](https://img.shields.io/badge/license-CC0--1.0-blue)](https://github.com/moyomogi/python_2022_lib/blob/master/LICENSE)

# 🐍 python_2022_lib

競技プログラミング用のライブラリ (Python)  
[Library](https://python-2022-lib.netlify.app/)

## localhost にサーブする方法

[Setup digital-garden-with-jekyll](https://maximevaillancourt.com/blog/setting-up-your-own-digital-garden-with-jekyll) を参考にしました。

必要なツールをインストール (初回のみ実行すればよい)。

```sh
# jekyll は ruby で実装されているので ruby をインストール。
sudo apt install -y ruby-dev ruby-bundler
gem install jekyll
```

以下を実行すれば、lib 配下を [localhost:4000](http://localhost:4000) にサーブできる。

```sh
# lib 配下のファイルを参照し、
# dist/_notes, dist/_pages 配下に Markdown 生成。
python3 generate_notes.py
cd dist

# dist/_notes, dist/_pages 配下のファイルを参照し、
# dist/_site 配下に html などを生成。
sudo bundle
# dist/_site 配下のファイルを
# http://localhost:4000 にサーブする。
sudo bundle exec jekyll serve
```

## 使用したテンプレート

[maximevaillancourt/digital-garden-jekyll-template](https://github.com/maximevaillancourt/digital-garden-jekyll-template)

## License

- `docs`, `lib` 配下のファイルは [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.ja) で許諾されています。すなわち、引用元に記載せずに、これらのファイルの一部または全部を使用できます。
- `dist` 配下のファイルは、使用したテンプレート [maximevaillancourt/digital-garden-jekyll-template] のライセンスである [MIT](https://github.com/maximevaillancourt/digital-garden-jekyll-template/blob/master/LICENSE) を継承します。すなわち、`dist` 配下のファイルの一部または全部を用いた場合は [maximevaillancourt/digital-garden-jekyll-template] を利用した旨を記載する必要があります。

[maximevaillancourt/digital-garden-jekyll-template]: https://github.com/maximevaillancourt/digital-garden-jekyll-template
