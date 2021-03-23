from collections import _heapq as heap
import unittest


# title method on strings
# a = "hello asdfkşas dasdf jkasdfl asd"
# print(a.title())
# a = a.strip()
# print(a)
print("2" > "10")
def changeArr(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] * 3


arr = [1,4,3,6,9]
changeArr(arr)
print(arr)
print("100" > "2")

class Survey: 

    def __init__(self,question): 
        self.question = question
        self.votes = []
    
    def insertVote(self,vote):
        self.votes.append(vote)

    def showQuestion(self):
        print(self.question)

    def showResults(self):
        for result in self.votes:
            print(f"- {result}")
    

class SurveyTestCase(unittest.TestCase):
    """inserting vote into the survey"""

    def setUp(self):
        question = "How are you?"
        self.survey = Survey(question)

        self.votes = ["Frightened", "Cheerful", "Sorrowful"]

        self.survey.insertVote(self.votes[0])
        self.assertIn(self.votes[0], self.survey.votes)


    def test_insert_vote(self):
        question = "How are you?"

        survey = Survey(question)
        survey.insertVote("good")

        self.assertIn("good",survey.votes)

    def test_insert_three_votes(self):
        question = "How are you?"
        survey = Survey(question)

        votes = ["Good", "Bad", "Joyful", "Upset"]
        for vote in votes: 
            survey.insertVote(vote)

        for vote in votes: 
            self.assertIn(vote, survey.votes)
            
        for vote in self.votes: 
            self.survey.insertVote(vote)
        
        for vote in self.votes: 
            self.assertIn(vote, self.survey.votes)


class Employee: 

    def __init__(self, fname, lname, salary): 
        self.firstName = fname 
        self.lastName = lname
        self.salary = salary 

    def give_raise(self, amount = 5000):
        self.salary += amount


class EmployeeTestCase(unittest.TestCase): 

    def setUp(self):
        self.employee = Employee("alp","niksarlı",40000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary,45000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.salary,50000)

def hw(n):
    if n<=1:
        return 8500000

    return hw(n-1) + (hw(n-1)/50) + 50000

def city_country(city,country, population=0):
    if population:
        return f"{city}, {country} - population {population}"
    str = f"{city}, {country}"
    result = str.title()
    return result

class TitleTestCase(unittest.TestCase):
    """testing my math homework
        recursive function"""

    def test_city_country(self):
        """testing the city_country function"""
        result = city_country("Istanbul","Turkey",15000000)

        self.assertEqual(result, "Istanbul, Turkey - population 15000000")
        

    def test_math_hw(self):
        """does the first test case work?"""
        result = hw(1)

        self.assertEqual(result,8500000)


if __name__ == "__main__":
    unittest.main()
        

print((1) * 3)

print(hw(6)) 

print(hash("alp"))
print(hash("0"))


print("ajsdf"[::2])

# codeforces first contest success
"""
def arrayDenser(arr,n):
    counter = 0
    for i in range(len(arr)-1):
        dense = False
        denseRatio = max(arr[i],arr[i+1]) / min(arr[i],arr[i+1])
        if denseRatio <= 2: 
            dense = True
        else: 
            import math
            counter += math.ceil(math.log2(denseRatio)) - 1
            
    return counter

n = int(input())
for i in range(n):
    length = int(input())
    arr = list(map(int, input().split()))
    count = arrayDenser(arr,length)
    print(count)
    
"""