from flask import Flask
app = flask(__name__)

if __name__=="__main__":
	app.run(debug=True)

@app.route('/application-form')
def application_blank():
	return render_template('application-form.html')


@app.route('/application')
def application_submitted():
	firstname = request.args.get("firstname")
	lastname = request.args.get("lastname")
	jobApplyingFor = request.args.get("firstname")
	salaryRequirement = request.args.get("salaryRequirement")

	return render_template('application.html', firstname=firstname, lastname=lastname, jobApplyingFor=jobApplyingFor, salaryRequirement=salaryRequirement)