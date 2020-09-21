from django.forms import ModelForm #ModelForm 사용하기
from .models import Post

# class PostForm(forms.Form):
#     title = forms.CharField(max_length =50, null=False)
#     content = forms.CharFiled(widget= forms.Textarea)
# 
# + TextField >> CharField로 바뀜 (FormField에서는)
# >> 이거는 그냥 form일 때

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
            #입력 받고 싶은 것만 지정
        ]
        # exclude = [
        #     'view_count',
        #     'user',
        #     'like_user_set',
        #     'created_at',
        #     'updated_at',
        # ] >>이렇게 제외할 것을 써도 결과는 같음
        
        # fields = '__all__'
        # 다 가져오고 싶을 때

        # exclude = [
        #     'title',
        # ]
        # exclude가 fields보다 우선

        labels = {
            'title': ('제목'),
            'content': ('내용'),
            'image': ('이미지'),
        } #input 태그 안에 뭐가 들어가는지 라벨로 알려줌
        help_texts = {
            'title': ('제목을 입력하세요'),  #입력 칸 오른 쪽에 설명 뜨게
            'content': ('내용을 입력하세요')
        }


    def save(self, **kwargs):
        post = super().save(commit=False) #데이터가 db에 바로 저장 되지 않음/ 그 전에 user 데이터 보내줘야 함
        post.user = kwargs.get('user', None) #kwargs로 넘어온 인자 중에서 user라는 항목 있음
        post.save()
        return post # 이렇게 보내주면>> views.py form에 저장 >> 이제 모델에 저장됨



    


