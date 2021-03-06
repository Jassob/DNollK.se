from django.db import models


class Document(models.Model):
    title = models.TextField()
    body = models.TextField()
    ordering = models.IntegerField(blank=True, null=True)

    def _render_base(self, isFirst):
        html = ["<div class=\"card center-text\">",
                "<h4><i>" + self.title + "</i></h4>",
                "<p>" + self.body + "</p>",
                "</div>"]

        if isFirst:
            html.insert(1, "<h1>Dokument</h1>")
            html.insert(2, "<hr>")
        return "\n".join(html)

    def render_with_heading(self):
        return self._render_base(True)

    def render(self):
        return self._render_base(False)

    def __str__(self):
        return self.title
