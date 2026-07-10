class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            t_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                t_sum += digit ** 2
            return t_sum

        slow = n
        fast = get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1
