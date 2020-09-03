from django.db import models

class Post(models.Model):
    contents = models.TextField('글내용', max_length = 1000)
    author = models.CharField('작성자', max_length = 20)

    def __str__(self):
        return self.contents

class Comment(models.Model):
    contents_comment = models.TextField('댓글내용', max_length = 1000)
    author_comment = models.CharField('댓글 작성자', max_length = 20)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.contents_comment