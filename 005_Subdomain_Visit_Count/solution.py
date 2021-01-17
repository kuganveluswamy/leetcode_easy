class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = {}
        result = []
        # Split to get count, loop though each domain levels and increament 
        for cpdomain in cpdomains:
            data = cpdomain.split(' ')
            count = int(data[0])
            levels = data[1].split('.')
            for i in range(len(levels)):
                domain = '.'.join(levels)
                if domain not in domain_count:
                    domain_count[domain] = 0
                domain_count[domain] += count
                levels.pop(0)
        # Convert dictionary data into a count-paired domain list
        for key in domain_count:
            result.append(str(domain_count[key]) + ' ' + key)
        return result
