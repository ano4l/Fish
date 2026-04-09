import urllib.request

urls = {
    "unsplash_mussels_a": "https://images.unsplash.com/photo-1560717789-0ac7c58ac90a?w=600&q=80",
    "unsplash_oyster_a": "https://images.unsplash.com/photo-1606731219412-4a17e55fa857?w=600&q=80",
    "unsplash_oyster_b": "https://images.unsplash.com/photo-1572402230267-f3e267c1e681?w=600&q=80",
    "unsplash_seafood_raw_a": "https://images.unsplash.com/photo-1615141982883-c7ad0e69fd62?w=600&q=80",
    "unsplash_seafood_raw_b": "https://images.unsplash.com/photo-1559737558-2f5a35f4523b?w=600&q=80",
    "unsplash_seafood_ice": "https://images.unsplash.com/photo-1498654200943-1088dd4438ae?w=600&q=80",
    "unsplash_mussels_b": "https://images.unsplash.com/photo-1586722840949-07cc88e79aa0?w=600&q=80",
    "unsplash_raw_fish_spread": "https://images.unsplash.com/photo-1610540881876-76de4d592c77?w=600&q=80",
    "unsplash_shellfish": "https://images.unsplash.com/photo-1448043552756-e747b7a2b2b8?w=600&q=80",
    "unsplash_oyster_c": "https://images.unsplash.com/photo-1587735243615-c03f25aaff15?w=600&q=80",
}

for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        code = urllib.request.urlopen(req, timeout=5).getcode()
        print(f"OK  {name}: {code} -> {url}")
    except Exception as e:
        print(f"FAIL {name}: {e}")
