from tornado import template
from tornado.web import authenticated

from cutthroat.handlers import ViewHandler


class Join(ViewHandler):

    """Join"""

    @authenticated
    def get(self):
        self.render("joinaroom.html")


class Create(ViewHandler):

    """Create"""

    @authenticated
    def get(self):
        self.render("createaroom.html")
