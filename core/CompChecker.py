import requests, sys, time, threading

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0',
                       'Accept': '*/*'}


def CompChecker(url, proxy):
    try:
        comdb = open('core/compDB', 'r').read().splitlines()
    except Exception, e:
        print('Error: ' + str(e))
        return ' [ Error in Scan ]'
    Comps = []
    def STarTScaN(url, com, proxy):
        try:
            rr = requests.get('http://' + url + '/index.php?option=' + com, timeout=10, headers=headers, proxies=proxy)
            if rr.status_code != 404:
                Comps.append(com)
        except Exception, e:
            pass
    x = 1
    thread = []
    for com in comdb:
        print(str(len(comdb)) + str('|') + str(x)),
        sys.stdout.flush()
        print("\r"),
        t = threading.Thread(target=STarTScaN, args=(url, com, proxy))
        t.start()
        thread.append(t)
        time.sleep(0.08)
        x = x + 1
    for j in thread:
        j.join()
    return Comps


