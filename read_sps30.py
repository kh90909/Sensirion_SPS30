from sps30 import SPS30

s = SPS30(port='/dev/ttyS0', save_data=False)

while True:
    r = s.run_query()
    if r:
        print(r)
