from flask import request, render_template, redirect
from rq.job import Job
from config import app, q
from worker import conn
from forms import UrlInputForm
from models import Counter

# Home page view
@app.route('/', methods=['GET', 'POST'])
def home():
	result = None
	form = UrlInputForm(request.form)
	if (request.method == 'POST'):
		if (form.validate_on_submit()):
			input_url = form.url.data
			job = q.enqueue_call(func='utils.count_words_at_url', args=(input_url,), result_ttl=5000)
			job_id = job.get_id()
			print('Job ID: ', job_id)
			return render_template('index.html', form=form, data=job_id)
		else:
			print('form is invalid')
	return render_template('index.html', form=form)

# get the corresponding count in url using job_key
@app.route("/results/<job_key>", methods=['GET'])
def get_results(job_key):
	job = Job.fetch(job_key, connection=conn)
	print(job_key)
	if (job.is_finished):
		obj = Counter.query.filter_by(id=job.result).first()
		print(obj.word_count)
		return render_template('word_count.html', data=str(obj.word_count))
	else:
		return "Refresh the page to see the results"
	return render_template('word_count.html', data=str(obj.word_count))