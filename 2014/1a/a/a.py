def solve_case(outlets, devices, N, L):
    total_outlet_flow = []
    total_device_flow = []

    for l in reversed(xrange(L)):
        outlet_flow = sum((outlet & (1 << l)) >> l for outlet in outlets)
        device_flow = sum((device & (1 << l)) >> l for device in devices)
        total_outlet_flow.append(outlet_flow)
        total_device_flow.append(device_flow)

    switches = 0
    for l in xrange(L):
        if total_device_flow[l] == total_outlet_flow[l]:
            continue
        elif total_device_flow[l] == N - total_outlet_flow[l]:
            switches += 1
        else:
            print 'NOT POSSIBLE'
            return
    print switches

def main():
    T = int(raw_input())
    for t in xrange(T):
        N, L = map(int, raw_input().split())
        outlets = map(lambda x: int(x, 2), raw_input().split())
        devices = map(lambda x: int(x, 2), raw_input().split())
        print 'Case #{}:'.format(t + 1),
        solve_case(outlets, devices, N, L)

if __name__ == '__main__':
    main()
