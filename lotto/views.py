from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm
# Create your views here.
#request : url 요청을 통해 받아들여오는 함수 제작.
def index(request):
    lottos=GuessNumbers.objects.all()
    #return render(request,'',[])#render ''=>돌려보내줄 주소 []=> 파이썬 변수를 사용할 때의 dict(key값으로 html에 넘겨준다 ex.'df':main_df) html에서 파이썬 코드를 박아줄 수 있다.
    return render(request,'lotto/default.html',{'lottos':lottos}) #보내줄 변수가 없으므로!(random함수만 사용하므로)
#http를 직접 보낼 때 일반적으로는 html 파일을 보내준다.
def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>") #HttpResponse는 임시

    #render ''=>돌려보내줄 주소 []=> 파이썬 변수를 사용할 때의 dic

def post(request):

    if request.method == 'POST':
        #빈 양식을 채워넣는다.(user가 제출한 데이터를 기반으로 채워진 양식 생성)
        form = PostForm(request.POST)
        if form.is_valid(): #양식이 기본적으로 가지고 있는 함수 max_length가 넘기지 않는가.
            lotto = form.save(commit=False)
            lotto.generate()
            return redirect('index')
        #속의 내용물을 직접 꺼내서 사용할 때/form 양식을 사용하지 않고!
        # user_name = request.POST['name']
        # user_text = request.POST['text']
        # row = GuessNumbers(name=user_name, text=user_test)
        # row.generate() # self.save()
        #print('\n\n\n===========================\n\n\n')
        #print(request.POST['csrfmiddlewaretoken'])
        #print(request.POST['name'])
        #print(request.POST['text'])
        #print('\n\n\n===========================\n\n\n')

    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form':form})

def detail(request,lottokey):
    lotto=GuessNumbers.objects.get(id=lottokey)
    return render(request,'lotto/detail.html',{'lotto':lotto})
