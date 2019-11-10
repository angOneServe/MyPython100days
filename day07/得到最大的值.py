def max2(nums):
    m1,m2=(nums[0],nums[1]) if nums[0]>nums[1] else(nums[1],nums[0] )
    for x in nums:
        if x>m1:
            m2=m1
            m1=x
        elif x>m2:
            m2=x
    return m1,m2

print (max2((1,2,-5,3,534,821,2)))
