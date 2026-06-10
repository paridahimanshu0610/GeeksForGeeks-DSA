class Solution:
    def myMergeSort(self, a, l, r, temp):
        n = r - l + 1
        if n == 1:
            return
        
        mid = (r+l)//2
        self.myMergeSort(a, l, mid, temp)
        self.myMergeSort(a, mid+1, r, temp)
        
        i, j = l, mid + 1
        k = l
        while i <= mid and j <= r:
            if a[i] <= a[j]:
                temp[k] = a[i]
                i += 1
            else:
                temp[k] = a[j]
                j += 1
            k += 1
        
        while i <= mid:
            temp[k] = a[i]
            k += 1
            i += 1
            
        while j <= r:
            temp[k] = a[j]
            k += 1
            j += 1
        
        k = l
        for i in range(l, r+1):
            a[i] = temp[k]
            k += 1
            
    def mergeSort(self, a, l, r):
        temp = [None]*len(a)
        self.myMergeSort(a, l, r, temp)