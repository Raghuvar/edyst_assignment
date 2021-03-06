from config import db

# database model
class Counter(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.String, nullable=False)
	word_count = db.Column(db.Integer, nullable=False)


	def __repr__(self):
		return '{0} contains {1} words'.format(self.url, self.word_count)