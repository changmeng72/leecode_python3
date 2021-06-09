 class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return 1-int(coordinates[1])%2 if ord(coordinates[0])%2 else int(coordinates[1])%2
        """
        if(ord(coordinates[0])%2):
                return 1-int(coordinates[1])%2
        else:
            return int(coordinates[1])%2
        """