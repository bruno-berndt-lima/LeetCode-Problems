class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {course: [] for course in range(numCourses)}

        for course, pre in prerequisites:
            adj_list[course].append(pre) 

        for course in range(numCourses):
            stack = [(course, set())]

            while stack:
                curr_course, visited = stack.pop()
                if curr_course in visited:
                    return False # cycle detected
                visited.add(curr_course)

                for pre in adj_list[curr_course]:
                    stack.append((pre, visited.copy()))

            # remove course
            adj_list[course] = []

        return True
