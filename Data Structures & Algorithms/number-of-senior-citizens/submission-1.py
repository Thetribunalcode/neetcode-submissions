class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([int(detail[11:13]) for detail in details if int(detail[11:13]) > 60])
        