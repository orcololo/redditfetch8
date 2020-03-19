from concurrent.futures import ThreadPoolExecutor as PoolExecutor

import wget


def download_file(url):
    wget.download(url)


def concurrent_download(links):
    with PoolExecutor(max_workers=16) as executor:
        executor.map(download_file, links)
        pass