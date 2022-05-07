import pandas as pd
!git clone https://github.com/blue0912/GOHAN-recommend.git

#集めたデータの確認、データフレームに落とす
df=pd.read_csv('/content/GOHAN-recommend/gohan - シート1.tsv',sep='\t',header=None)
df.head()

#日付削除日付削除
df=df.drop(0,axis=1)

#MeCabインストール
!pip install mecab-python3
!pip install unidic
!python -m unidic download

#分かち書きのdef
def wakati(x):
  return MeCab.Tagger('-Owakati').parse(x).replace('\n','')

#空のデータフレームデータフレーム
df_wakati = pd.DataFrame()
print(df_wakati)

#分かちがきにする
import MeCab
import unidic

for index, row in df.iterrows():
    #print(row[1],row[2])
    waka=[(wakati(row[1]),wakati(row[2]))]
    df_wakati=df_wakati.append(waka)
    
#確認
df_wakati.head()

#励ましコーパスのデータ
df_hage=pd.read_csv('/content/bigsns-wakati.tsv',sep='\t',header=None)
df_hage.head()

#二つのデータフレームを結合
df_gohan = pd.concat([df_wakati, df_hage], axis=0)
df_gohan

# tsvファイルに出力(TSV形式でindexを出力しない場合)
df_gohan.to_csv('df_gohan.tsv', sep='\t', index=False)
