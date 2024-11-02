class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        c=0
        p=0
        for i in range(len(sentence)):
            if(sentence[i]==' '):
                c+=1
                if(sentence[i-1]==sentence[i+1]):
                    p+=1
        if(c==p and sentence[-1]==sentence[0]):
            return True
        return False


        