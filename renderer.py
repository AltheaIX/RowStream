def render_page(rows, current_page, total_pages):

    for r in rows:
        print("{0}. Name: {1}, ".format(r.id, r.nama))

    print("Current page: {0}/{1}".format(current_page+1, total_pages))