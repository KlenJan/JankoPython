class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes


c = Comment("davey123", "lol you're so silly", 3)
c. username  # "davey123"
c. text  # "lol you're so silly"
c.likes  # 3
another_comment = Comment("rosa77", "soooo cute!!!")
another_comment.username  # "rosa77"
another_comment.text  # "soooo cute!!!"
another_comment.likes  # 0
