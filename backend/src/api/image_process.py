import easyocr


def main():
    reader = easyocr.Reader(['pt'])
    content = reader.readtext("/Users/gabsvieira/projects/splitscreen/backend/images/test_1.jpeg", detail=0, paragraph=True)



if __name__ == "__main__":
    main()