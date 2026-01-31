class Solution:
    def nextGreatestLetter(self, a: List[str], t: str) -> str:
        return (a*2)[bisect_right(a,t)]