import os
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    # hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    # head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    # file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self): 
        return f'[{self.pk}]{self.title}' # 포스트의 제목이 나오도록 함. pk는 각 레코드에 대한 고유값으로 처음에는 1이 자동으로 부여도고 1씩 증가함.   

    def get_absolute_url(self): # 객체의 상세 페이지로 이동할 수 있는 링크를 만들 수 있음. url 생성 규칙을 정의하는 메서드
        return f'/blog/{self.pk}/'