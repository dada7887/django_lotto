from django.db import models
from django.utils import timezone #시간대를 꺼내주는 것(settings.py의 timezone이 기준이 된다.)
import random

# Create your models here.
class GuessNumbers(models.Model): #TABLe이름 미리 존재하는(장고에 이미 존재하는) 모델을 상속받아 사용한다.
    #열마다 이름을 지정해준다. #max_length:제약조건, default도 함께 적용할 수 있다.
    #non-null 제약조건이 없기 때문에 결측치로 빈값이 들어간다(sql처럼!!!)
#def __init__(self): class-생성자 함수처럼 이미 존재하고 있는 함수이다! - 이미 존재하고 있는 함수를 수정하는 것!
    name = models.CharField(max_length=24) # 로또 번호 리스트의 이름
    text = models.CharField(max_length=255) # 로또 번호 리스트에 대한 설명
    lottos = models.CharField(max_length=255, default='[1, 2, 3, 4, 5, 6]') # 로또 번호들이 담길 str
    num_lotto = models.IntegerField(default=5) # 6개 번호 set의 갯수
    update_date = models.DateTimeField()
#row_1=GuessNumbers() print(row_1.name)=열에 대응. 빈값이므로 결측치 출력 print(row_1):__str__의 결과가 출력
#머신러닝 모델에서 model print를 하면 설명이 나오는 것도 동일한 원리인 것.//ex)print(model)=>LinearRegrssion() 출력
    #generate함수는 views.py에서 정의한 후 models.py에서 불러와도 됨! row_1.generate 문자열 저장.
    def generate(self): # 로또 번호를 자동으로 생성
        self.lottos = ""
        origin = list(range(1,46)) # 1~46의 숫자 리스트
        # 6개 번호 set 갯수만큼 1~46 뒤섞은 후 앞의 6개 골라내어 sorting
        for _ in range(0, self.num_lotto):#index를 딱히 사용할 일이 없으면 _를 이용한다.
            random.shuffle(origin) #섞어준다.
            guess = origin[:6]
            guess.sort()
            self.lottos += str(guess) +'\n' # 로또 번호 str에 6개 번호 set 추가,문자열로 변경.
        self.update_date = timezone.now()
        self.save() # GuessNumbers object를 DB에 저장=> sql commit
#생성자 함수처럼 이미 존재하는 함수.
#행에 대해 print했을 때의 결과//관리자 페이지에서의 출력 결과가 바뀌게 된다.
#print(non_str)=> Object GuessNumbers~~~~가 출력, 관리자 페이지에서 위와 같이 클래스 이름과 메모리가 출력된다.
#str 함수를 수정하는 것=> 출력되는 return 값을 수정하는 것!
    def __str__(self): # Admin page에서 display되는 텍스트에 대한 변경
        return "pk {} : {} - {}".format(self.pk, self.name, self.text) # pk는 자동생성됨 primary key는 자동 생성된다.(id)
        #물려받은 model 클래스에 이미 id변수가 정의되고 있기 때문!(self.pk)=(self.id): 동일한 열이 뽑혀져 나온다.(primary key변경은 가능함.)
   #def str(self): # Admin page에서 display되는 텍스트에 대한 변경
        #return "안녕하세요!!!" # pk는 자동생성됨


#row_1 = GuessNumbers()
#print(row_1.name) #
#print(row_1.lottos) # '[1, 2, 3, 4, 5, 6]'

#print(row_1) # <Object GuessNumbers ~~~
#print(row_1) # "안녕하세요!!!"

#model = linear_model.LinearRegression()
#row_1 = GuessNumbers()
#row_1.generate()
#print(row_1.num_lotto) # 5
