class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            alive = True
            while alive and asteroid < 0 and stack and stack[-1] > 0:
                if abs(asteroid) == stack[-1]:
                    stack.pop()
                    alive = False
                elif abs(asteroid) < stack[-1]:
                    alive = False
                else:
                    stack.pop()
            if alive:
                stack.append(asteroid)
        
        return stack

            