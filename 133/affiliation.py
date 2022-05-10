def generate_affiliation_link(url):
    id = url.lstrip('https://').split('/')[3]

    return f'http://www.amazon.com/dp/{id}/?tag=pyb0f-20'
