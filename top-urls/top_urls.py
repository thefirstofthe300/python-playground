def GetHostname(url):
  split_url = url.split("/")
  print split_url
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

