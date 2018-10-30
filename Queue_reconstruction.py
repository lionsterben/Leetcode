class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ind = {}
        if not people:
            return []
        #首先确定最小的0是第一个，然后算出前方比他大和现有比他小的即为现在位置
        res = []
        res.append(None)
        cc = people.copy()
        st = 0
        min_res = 10000000
        for i in people:
            if i[1] == 0 and i[0] < min_res:
                res[0] = i
                min_res = i[0]
        cc.remove(res[0])
        while cc:
            dd = 10000000
            gaga = None
            st += 1
            for i in cc:
                ind = 0
                for j in res:
                    if i[0] > j[0]:
                        ind += 1
                if ind+i[1] == st:
                    if i[0] < dd:
                        gaga = i
                        dd = i[0]
            res.append(gaga)
            cc.remove(gaga)
                    
        return res

class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people:
            return []
        people.sort(key = lambda x:[-x[0], x[1]])
        res = []
        for [h,k] in people:
            res.insert(k, [h,k])
            # print(res)
        return res

k值依赖大于等于它的其他值确定，我们首先对[h,k]里的h进行逆序排序，最大的h按照k值顺序排序。之后逐渐变小的h按照自己的k值插入（小的k先插入，因为小的k会对大的k产生影响），因为之后不会有更大的值插入（不会影响当前插入的相对位置），而且现在插入的h必然小于之前插入的，所以不会对之前插入的产生影响。