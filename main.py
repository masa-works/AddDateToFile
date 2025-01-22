import os
import sys
from datetime import datetime

def add_date_to_filename(file_path, include_time=False):
    """
    ファイル名に日付を追加し、オプションで時間も追加します。

    Args:
        file_path (str): 処理対象のファイルパス。
        include_time (bool): Trueの場合、時間も追加します。
    """
    try:
        # ファイルのパスと名前を分割
        folder_path, full_filename = os.path.split(file_path)
        filename, ext = os.path.splitext(full_filename)

        # 日付（および時間）のフォーマット設定
        if include_time:
            datetime_suffix = datetime.now().strftime("%Y%m%d%H%M_")
        else:
            datetime_suffix = datetime.now().strftime("%Y%m%d_")

        # 新しいファイル名を生成
        new_filename = f"{datetime_suffix}{filename}{ext}"
        new_file_path = os.path.join(folder_path, new_filename)

        # ファイル名を変更
        os.rename(file_path, new_file_path)
        print(f"ファイル名を変更しました: {new_file_path}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ファイルを指定してください。")
        sys.exit(1)

    file_path = sys.argv[1]
    # フラグ引数の処理: デフォルトは False
    include_time = "--time" in sys.argv
    add_date_to_filename(file_path, include_time)
