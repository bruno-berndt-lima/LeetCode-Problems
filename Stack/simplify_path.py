class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split("/")
        stack = []

        for split in split_path:
            if split == "..":
                if stack:
                    stack.pop()
            elif split != "" and split != ".":
                stack.append(split)
        
        simplified_path = ""
        for split in stack:
            simplified_path += "/" + split

        return simplified_path if simplified_path != "" else "/"
