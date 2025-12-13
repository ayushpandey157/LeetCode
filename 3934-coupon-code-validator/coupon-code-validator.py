class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        return [c for c, _ in sorted([(c, b) for c, b, a in zip(code, businessLine, isActive) if len(c)>0 and all(cc.isalnum() or cc == '_' for cc in c) and b in ["electronics", "grocery", "pharmacy", "restaurant"] and a], key = lambda x: (x[1], x[0]))]        