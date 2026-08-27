class Solution:
    def countSeniors(self, details: List[str]) -> int:
        num_of_senior_citizens = 0
        for customer_detail in details:
            age = int(customer_detail[11:13])
            if age > 60: 
                num_of_senior_citizens += 1
        return num_of_senior_citizens