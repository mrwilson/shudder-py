class Media(object):
    def __init__(self, title, media_id):
        self.title = title
        self.id = media_id.split("/")[-1]


class Movie(Media):
    def __repr__(self):
        return "<Movie [id=%s, title=%s]>" % (self.id, self.title)


class Series(Media):
    def __repr__(self):
        return "<Series [id=%s, title=%s]>" % (self.id, self.title)
