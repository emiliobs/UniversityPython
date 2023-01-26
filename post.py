class Post:
    def __init__(csc, message, author):
        csc.message = message
        csc.author = author


    def get_post_info(csc):
        print(f"Post: {csc.message} written by : {csc.author}")
    
    def change_post_author(csc, author):
        csc.author = author
