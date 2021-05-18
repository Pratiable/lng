class NumberError(Exception):
    def __init__(self):
        super().__init__('숫자를 잘못 입력하셨습니다.')


class LottoNumberGenerator:
    def __init__(self, manualnum):
        self.start = manualnum
        self.maxnum = 6
        self.manualnum = manualnum
        self.mlist = []
        self.numberset = list(map(int, set(str(i) for i in range(1, 46)))) #세트의 인덱스 사용을 위해 리스트로 변환

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.maxnum and self.manualnum == 0: # 자동
            n = self.numberset[self.start]
            self.start += 1
            return n
        elif self.start < self.maxnum and 0 < self.manualnum < 6: # 반자동
            if not len(self.mlist):
                self.mlist = list(map(int, input('위에 입력한 개수만큼 수동으로 사용할 번호 입력 (공백으로 구분): ').split()))
                if len(set(self.mlist)) != self.manualnum or max(self.mlist) > 45 or min(self.mlist) < 1:
                    raise NumberError
                self.numberset = [i for i in self.numberset if i not in self.mlist] # 수동으로 넣은 번호 삭제
                return self.mlist
            n = self.numberset[self.start]
            self.start += 1
            return n
        elif self.manualnum > 5 or self.manualnum < 0:
            raise NumberError
        else:
            raise StopIteration


Mnum = int(input('자동은 "0" 입력 반자동은 "1 - 5"사이 입력 : '))
output = []
for i in LottoNumberGenerator(Mnum):
    if type(i) == list:
        output += i
    else:
        output.append(i)
output.sort()
print('추천 번호는', output, '입니다!')
