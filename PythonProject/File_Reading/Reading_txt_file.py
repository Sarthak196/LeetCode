import os

def read_txt_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        words = 0
        for line in lines:
        # Print each line without extra spaces or newlines
        # -------------------------------------------------------------------------------------------------------------
            res = line.split('.')
            for r in res:
                print(r.strip())
        # -------------------------------------------------------------------------------------------------------------
            # count the number of words in the file
        # -------------------------------------------------------------------------------------------------------------
        #     res = line.split()
        #     words+= len(res)
        # print(f"Number of words in the file: {words}")
        # -------------------------------------------------------------------------------------------------------------



if __name__ == "__main__":
    file_path = 'sample.txt'
    try:
        read_txt_file(file_path)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print("An error occurred:", e)