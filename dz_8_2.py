import re


operation = re.compile(r'((?:\d+\.){3}\d+)\W+(\d+.\w+.\d{4}.\d{2}.\d{2}.\d{2}\s.\d{4})'
                       r'\W+([A-Z]+)\s(\S+)\s\S+\s(\d+)\s(\d+)')
example = '93.180.71.3 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1"' \
          ' 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"'
example_list = operation.findall(example)
print(*example_list)
