import os
import sys
from datetime import datetime

def add_date_to_filename(file_path, include_time=False, include_folder=False):
    """
    ファイル/フォルダ名に日付を追加し、オプションで時間も追加します。

    Args:
        file_path (str): 処理対象のファイルパス。
        include_time (bool): Trueの場合、時間も追加します。
    """
    if include_folder:
        try:
            # ファイルのパスと名前を分割
            folder_path, foldername = os.path.split(file_path)

            # 日付（および時間）のフォーマット設定
            if include_time:
                datetime_suffix = datetime.now().strftime("%Y%m%d%H%M_")
            else:
                datetime_suffix = datetime.now().strftime("%Y%m%d_")

            # 新しいファイル名を生成
            new_foldername = f"{datetime_suffix}{foldername}"
            new_folder_path = os.path.join(folder_path, new_foldername)

            print(new_foldername)
            print(new_folder_path)

            # ファイル名を変更
            os.rename(file_path, new_folder_path)
            print(f"フォルダ名を変更しました: {new_folder_path}")
        except Exception as e:
            print(f"エラーが発生しました: {e}")
    else:
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
        print("ファイル/フォルダを指定してください。")
        sys.exit(1)

    file_path = sys.argv[1]
    # フラグ引数の処理: デフォルトは False
    include_time = "--time" in sys.argv
    include_folder = "--folder" in sys.argv
    add_date_to_filename(file_path, include_time, include_folder)
