from django.test import TestCase
from django.test import TestCase
from .models import GuessNumbers

# Create your tests here.
class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        #한번의 성공/실패에 대한 판단
        g = GuessNumbers(name='Test numbers', text='selected numbers')
        #행 하나 만들기=> 만들면서 generate함수를 강제로 실행한다.
        #로또 번호 세트를 만들어준다./현재시간을 알려준다./db파일 반
        g.generate() # GuessNumbers 클래스의 generate 함수를 실행
        print(g.update_date)
        print(g.lottos)

        # 실제 Test case (OK or FAILED)
        # default로 6개 숫자 x 5set = 30개의 숫자가 생성됨을 확인
        self.assertTrue(len(g.lottos) > 300)#조건이 True이면 성공, False면 실패
        #다양한 조건문이 존재한다.
        #https://docs.djangoproject.com/en/4.0/topics/testing/tools/
# Create your tests here.
