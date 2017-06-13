def GetHostname(url):
  split_url = url.split("/")
  if len(split_url[0]) == 0:
    raise TypeError("URL protocol is not valid.")
  return split_url[2]

def GetHostnameCountsForUrls(urls):
  hostnames = {}
  for url in urls:
    hostname = GetHostname(url)
    if hostnames.get(hostname):
      hostnames[hostname] += 1
    else:
      hostnames[hostname] = 1
  return hostnames

def GetTopHostnames(hostnames):
  top_hostnames = {}
  hostnames_list = [(key, value) for key, value in hostnames.iteritems()]

  hostnames_list.sort(key=lambda x: x[1], reverse=True)

  for i in range(10):
    top_hostnames[hostnames_list[i][0]] = hostnames_list[i][1]

  return top_hostnames
