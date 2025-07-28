from sklearn.cluster import KMeans
import numpy as np

def cluster_font_sizes(line_items, n_clusters=4):
    # Extract unique font sizes
    unique_sizes = sorted({round(item["font_size"], 1) for item in line_items}, reverse=True)
    if not unique_sizes:
        return {}

    # If fewer sizes than clusters, reduce cluster count
    n = min(n_clusters, len(unique_sizes))
    sizes_np = np.array(unique_sizes).reshape(-1, 1)

    # Cluster font sizes
    kmeans = KMeans(n_clusters=n, random_state=42, n_init="auto")
    kmeans.fit(sizes_np)

    # Build cluster → font size map
    labeled_sizes = list(zip(kmeans.labels_, unique_sizes))
    # Sort by font size descending
    labeled_sizes.sort(key=lambda x: -x[1])

    # Map font size to heading level
    level_order = ["TITLE", "H1", "H2", "H3"]
    font_size_to_level = {}
    used = set()
    for idx, (_, size) in enumerate(labeled_sizes):
        if size in used:
            continue
        level = level_order[idx] if idx < len(level_order) else None
        if level:
            font_size_to_level[size] = level
            used.add(size)

    return font_size_to_level
