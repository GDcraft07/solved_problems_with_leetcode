class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = address.split('.')
        address = '[.]'.join(address)
        return address
