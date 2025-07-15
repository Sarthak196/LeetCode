import os

def write_file(file_path):
    # writing new lines to a file
    # -------------------------------------------------------------------------------------------------------------
    # if os.path.exists(file_path):
    #     with open(file_path, 'a', encoding='utf-8') as file:
    #         print("File opened in append mode. You can start entering lines.")
    #         while True:
    #             line = input("Enter a line to write to the file: ")
    #             if line.lower() == 'exit':
    #                 break
    #             file.write(line + '\n')
    # else:
    #     with open(file_path, 'w', encoding='utf-8') as file:
    #         print("File opened in write mode. You can start entering lines.")
    #         while True:
    #             line = input("Enter a line to write to the file: ")
    #             if line.lower() == 'exit':
    #                 break
    #             file.write(line + '\n')
    # -------------------------------------------------------------------------------------------------------------
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace('name', 'NAME')
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    # -------------------------------------------------------------------------------------------------------------



if __name__ == "__main__":
    file_path = 'output.txt'
    output_file_path = 'output1.txt'
    try:
        write_file(file_path)
    except FileExistsError:
        print(f"The file {file_path} already exists.")
    except Exception as e:
        print("An error occurred:", e)