from typing import List

from typing import List

class Solution_Best:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for asteroid in asteroids:
            alive = True

            # collision only when last moves right and current moves left
            while alive and st and st[-1] > 0 and asteroid < 0:
                top = st[-1]

                if abs(top) < abs(asteroid):
                    st.pop()          # top explodes, keep checking earlier ones
                    continue
                elif abs(top) == abs(asteroid):
                    st.pop()          # both explode
                    alive = False
                else:
                    alive = False     # current explodes

            if alive:
                st.append(asteroid)

        return st


class Solution_2nd_best:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for a in asteroids:
            alive = True
            a_size = -a if a < 0 else a

            while alive and st and st[-1] > 0 and a < 0:
                top = st[-1]
                top_size = top

                if top_size < a_size:
                    st.pop()
                elif top_size == a_size:
                    st.pop()
                    alive = False
                else:
                    alive = False

            if alive:
                st.append(a)

        return st


class Solution_initial_Approach:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for asteroid in asteroids:
            current_direction = -1 if asteroid < 0 else 1
            if current_direction == -1:
                alive = True
                while st and st[-1]>=0:
                    last_value = st.pop()
                    if abs(asteroid) == abs(last_value):
                        alive = False
                        break
                    elif abs(asteroid) < abs(last_value):
                        st.append(last_value)
                        alive = False
                        break
                if alive:
                    st.append(asteroid)
            else:
                st.append(asteroid)

        return st