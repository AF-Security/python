# file extension matching
# prompt user for the name of a file and then outputs that file's media type if the file's name ends, case-insensitively, with one of the following extensions: 
# .gif, .jpg, .jpeg, .png, .pdf, .txt, .zip
# if the file's name ends with none of those extensions or no suffix, output "application/octet-stream"

def main():
    file_name = input("File name:").casefold().strip()
    file_type(file_name)

def file_type(file):
    if file.endswith(".gif"):
        print("image/gif")
    elif file.endswith(".jpg") or file.endswith(".jpeg"):
        print("image/jpeg")
    elif file.endswith(".png"):
        print("image/png")
    elif file.endswith(".pdf"):
        print("application/pdf")
    elif file.endswith(".txt"):
        print("text/plain")
    elif file.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main()