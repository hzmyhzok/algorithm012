class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        排序
        '''
        if sorted(s) == sorted(t):
    	    return True
        else:
            return False


    '''
    哈希表
    import collections
    class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
            return collections.Counter(s) == collections.Counter(t)
    '''