class Media(object):
    def __init__(self, title, media_id, entity):
        self.title = title
        self.id = media_id.split("/")[-1]
        self.original = entity


class Movie(Media):
    def __repr__(self):
        return "<Movie [id=%s, title=%s]>" % (self.id, self.title)


class Series(Media):
    def __repr__(self):
        return "<Series [id=%s, title=%s]>" % (self.id, self.title)


class Review(object):
    def __init__(self, entity):
        self.id = entity["id"]
        self.score = entity["score"]
        self.content = entity["content"]
        self.title = entity["title"]
        self.created_at = entity["created_at"]
        self.user = entity["user"]["display_name"]
