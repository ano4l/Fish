import urllib.request

urls = {
    "oysters_half_shell": "https://images.pexels.com/photos/4553111/pexels-photo-4553111.jpeg?auto=compress&cs=tinysrgb&w=600",
    "raw_oysters_plate": "https://images.pexels.com/photos/8753447/pexels-photo-8753447.jpeg?auto=compress&cs=tinysrgb&w=600",
    "seafood_ice_mix": "https://images.pexels.com/photos/3731945/pexels-photo-3731945.jpeg?auto=compress&cs=tinysrgb&w=600",
    "raw_seafood_spread": "https://images.pexels.com/photos/3843224/pexels-photo-3843224.jpeg?auto=compress&cs=tinysrgb&w=600",
    "shrimp_raw_ice": "https://images.pexels.com/photos/7625056/pexels-photo-7625056.jpeg?auto=compress&cs=tinysrgb&w=600",
    "mussels_raw": "https://images.pexels.com/photos/2252584/pexels-photo-2252584.jpeg?auto=compress&cs=tinysrgb&w=600",
    "seafood_raw_display": "https://images.pexels.com/photos/1516415/pexels-photo-1516415.jpeg?auto=compress&cs=tinysrgb&w=600",
    "raw_seafood_platter": "https://images.pexels.com/photos/699953/pexels-photo-699953.jpeg?auto=compress&cs=tinysrgb&w=600",
}

for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        code = urllib.request.urlopen(req, timeout=5).getcode()
        print(f"OK  {name}: {code}")
    except Exception as e:
        print(f"FAIL {name}: {e}")
