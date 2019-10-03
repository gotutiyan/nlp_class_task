# テキスト分類器

文章がどんな話題について話しているかを推測するものです。索引語が抽出できているものとして作成しています。tf-idf法により重みづけしたデータに対して、k-近傍法を用いて、上位k件の話題を出力します。

この課題は[自然言語処理の基礎 (奥村学 - コロナ社)](https://www.amazon.co.jp/dp/4339024511/ref=cm_sw_r_tw_dp_U_x_xszLDb90TGPVE )のP122~を参考にしています。

* train.csv

  学習用のデータです。第一カラムに索引語が、第二カラムにその索引語が表す話題を記しています。これは僕が適当に決めています。

* input_index.csv

  実際に検証するデータです。文章から索引語をすでに抽出できているものとして、索引語が与えられています。１行につき1つの文章についての索引語という設定です。

各文章について、k-近傍法によって推測された話題を出力します。