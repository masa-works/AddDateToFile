## 【説明】
コンテキストメニューに機能を追加します。  
本ツールを使用することで任意のファイルに日付、日付と時間を追加することができます。

## 【手順】
### 1. レジストリエディタに情報を追加
以下ファイルを管理者として実行し、レジストリエディタに情報を追加します。

- AddDateToX_reg.exe

※ 問題なく追加できると 「インポート完了」 のメッセージが表示されます。

### 2. 動作確認
任意のファイル/フォルダを右クリックし、「ファイル名に日付を追加」/「フォルダ名に日付を追加」をクリックします。
ファイル/フォルダ名が変更されることが確認できます。
```
例: example.txt → 20250122_example.txt
    example_folder → 20250122_example_folder
```

※ 複数ファイル/フォルダに対しても実行可能です。

### ex. パス更新について
main.exeを任意のパスに変更した際は  
以下ファイルをmain.exeと同フォルダに配置し、管理者として実行してください。

- AddDateToX_reg.exe

※ 問題なく更新できると 「アップデート完了」 のメッセージが表示されます。  
※ **main.exeとAddDateToX_reg.exeは、必ず同じフォルダに配置してください。**  
※ **main.exeが同じフォルダに存在しない場合、エラーメッセージが表示されます。**
```
以下のようにmain.exeを移動させたい場合
例: C:\Users\%username%\Downloads\AddDateToX → C:\Users\%username%\Documents\AddDateToX
```
